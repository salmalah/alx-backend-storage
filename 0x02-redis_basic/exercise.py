#!/usr/bin/env python3
"""
This module is to define Cache
"""
from typing import Union
import redis
import uuid

class Cache:
    """
    This is Cache class using Redis
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance with a Redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store in input (data) in Redis using a random key (UUID) and return key

        Args:data (Union[str, bytes, int, float])

        Returns:
            str: The randomly generated key used for storing the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

# Example usage in main.py
if __name__ == "__main__":
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))
