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

    def get(self, key: str, fn: Callable = None)
    -> Union[str, bytes, int, None]:
        """
        Retrieve data from Redis using the provided key and apply

        Args:
            key (str): The key used
            fn (Callable, optional): The optional conversion function to apply

        Returns:
            Union[str, bytes, int, None]: The retrieved data
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve and convert data from Redis to a string.

        Args:
            key (str): The key used to retrieve data from Redis.

        Returns:
            Union[str, None]: The retrieved data as a string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve and convert data from Redis to an integer.

        Args:
            key (str): The key used to retrieve data from Redis.

        Returns:
            Union[int, None]: The retrieved data as an integer.
        """
        return self.get(key, fn=int)

# Example usage in main.py

if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
