#!/usr/bin/env python3
""" Redis Module """

import redis
import requests
from functools import wraps
from typing import Callable

redis_instance = redis.Redis()
'''The module-level Redis instance.
'''


def cache_data(method: Callable) -> Callable:
    '''Caches the output of fetched data with an expiration time of 10 seconds.
    '''
    @wraps(method)
    def invoke_and_cache(url) -> str:
        '''Wrapper function for caching the output.
        '''
        redis_instance.incr(f'access_count:{url}')
        cached_result = redis_instance.get(f'cached_result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')
        result = method(url)
        redis_instance.set(f'access_count:{url}', 0)
        redis_instance.setex(f'cached_result:{url}', 10, result)
        return result

    return invoke_and_cache

@cache_data
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    tracking the access count, and with an expiration time of 10 seconds.
    '''
    return requests.get(url).text

# Example usage:
if __name__ == "__main__":
    # Simulate slow response for testing
    slow_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    
    # Access the slow URL multiple times
    for _ in range(3):
        page_content = get_page(slow_url)
        print(page_content)

    # Access a different URL
    another_url = "http://www.example.com"
    page_content = get_page(another_url)
    print(page_content)
