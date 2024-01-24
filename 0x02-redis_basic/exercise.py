#!/usr/bin/env python3
"""
This module is to define Cache
"""
import redis
import uuid
from typing import Any, Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to track the number of calls
    """
    @wraps(method)
    def invoke_and_count(self, *args, **kwargs) -> Any:
        """
        Invokes the method after incrementing
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoke_and_count


def call_history(method: Callable) -> Callable:
    """
    Decorator to track the call details of a method in a Cache
    """
    @wraps(method)
    def invoke_and_log(self, *args, **kwargs) -> Any:
        """
        Return: method's output after storing its inputs and output
        """
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoke_and_log


def replay(fn: Callable) -> None:
    """
    Displays the call history of a Cache instance method
    """
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    method_name = fn.__qualname__
    in_key = '{}:inputs'.format(method_name)
    out_key = '{}:outputs'.format(method_name)
    method_call_count = 0
    if redis_store.exists(method_name) != 0:
        method_call_count = int(redis_store.get(method_name))
    print('{} was called {} times:'.format(method_name, method_call_count))
    method_inputs = redis_store.lrange(in_key, 0, -1)
    method_outputs = redis_store.lrange(out_key, 0, -1)
    for method_input, method_output in zip(method_inputs, method_outputs):
        print('{}(*{}) -> {}'.format(
            method_name,
            method_input.decode("utf-8"),
            method_output,
        ))


class Cache:
    """
    Cache class using Redis
    """
    def __init__(self) -> None:
        """Initializes a Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key (UUID) and return the key
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Retrieves a value from a Redis data storage.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        Retrieve and convert data from Redis to a string
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieve and convert data from Redis to an integer
        Returns: Union[int, None]: The retrieved data as an integer.
        """
        return self.get(key, lambda x: int(x))
