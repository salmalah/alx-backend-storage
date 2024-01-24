#!/usr/bin/env python3
"""
This module is to defile Redis Module
"""
import requests
import redis
from functools import wraps
from typing import Callable

# Initialize Redis client
redis_client = redis.Redis()

def cache_page(func: Callable) -> Callable:
    """
    Decorator for caching the result of a function with a specified expiration time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        url = args[0]  # Assuming the first argument is the URL
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"

        # Check if the result is cached
        cached_result = redis_client.get(cache_key)
        if cached_result is not None:
            # Increment access count
            redis_client.incr(count_key)
            return cached_result.decode("utf-8")

        # If not cached, call the original function
        result = func(*args, **kwargs)

        # Cache the result with a 10-second expiration time
        redis_client.setex(cache_key, 10, result)

        # Increment access count
        redis_client.incr(count_key)

        return result

    return wrapper

@cache_page
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a particular URL and return it.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text

# Example usage
if __name__ == "__main__":
    slow_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    fast_url = "http://www.google.com"

    # Access slow URL multiple times to test caching and access count
    for _ in range(3):
        print(get_page(slow_url))

    # Access fast URL to test caching and access count
    print(get_page(fast_url))

    # Sleep for more than 10 seconds to let the cache expire for the slow URL
    import time
    time.sleep(11)

    # Access slow URL again to test cache expiration
    print(get_page(slow_url))

    # Print access count for both URLs
    print(f"Access count for {slow_url}: {redis_client.get(f'count:{slow_url}')}")
    print(f"Access count for {fast_url}: {redis_client.get(f'count:{fast_url}')}")
