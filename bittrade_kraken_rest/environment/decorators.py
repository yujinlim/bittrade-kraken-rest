import importlib
from functools import wraps
from os import getenv


def with_api_key(func):
    @wraps(func)
    def fn(api_key: str = '', **kwargs):
        if not api_key:
            api_key = getenv('KRAKEN_API_KEY')
        if not api_key:
            raise ValueError('API key needs to be passed to methods or set as environment variable KRAKEN_API_KEY')
        return func(api_key=api_key, **kwargs)

    return fn
