import dataclasses
import importlib
import urllib.parse
from functools import wraps
from os import getenv
from rich.table import Table

import requests

try:
    from rich.console import Console

    console = Console()
except ImportError:
    console = None


def pretty_print(func):
    if not console:
        raise Exception('Pretty print can only be used with the [fire] version of the library')

    @wraps(func)
    def fn(*args, **kwargs):
        outcome: requests.Response = func(*args, **kwargs)
        request: requests.Request = outcome.request
        console.line()
        if outcome.ok:
            if not outcome.json()['error']:
                style = 'green'
            else:
                style = 'red'
        else:
            style = 'bold red'
        console.rule(request.url, style=style)
        if outcome.ok:
            console.print_json(outcome.text)
            console.line()
        else:
            console.print(f'Failed with status {outcome.status_code}')
        posted_data = urllib.parse.parse_qs(request.body)
        console.rule('Data sent:', style='cyan')
        table = Table('Name', 'Value')
        for k, v in posted_data.items():
            if k == 'nonce':
                continue
            table.add_row(k, v[0])
        console.print(table)
        console.line()
        console.rule('From request:', style='cyan')
        console.print(request.__dict__)
        console.line(2)

    return fn


def private(func):
    if not console:
        raise Exception('Pretty print can only be used with the [fire] version of the library')

    @wraps(func)
    def fn(*args, **kwargs):
        try:
            module = importlib.import_module(
                getenv('KRAKEN_SIGNATURE_MODULE', 'kraken_signature_generator')
            )
            generate_kraken_signature = module.generate_kraken_signature
        except (ImportError, AttributeError) as exc:
            console.bell()
            console.line()
            console.rule('Kraken signature implementation missing')
            console.print('''
                This library believes in BYOC (Bring Your Own Credentials).
                Implement the signature calculation yourself and export its module path to env [red]KRAKEN_SIGNATURE_MODULE[/red]
                You can simply copy from Kraken's official reference https://docs.kraken.com/rest/#section/Authentication/Headers-and-Signature
            ''')
            raise exc
        kwargs['generate_kraken_signature'] = generate_kraken_signature
        return func(*args, **kwargs)

    return fn


def kwargs_to_options(dataclass: dataclasses.dataclass, func):
    def fn(**kwargs):
        new_kwargs = {}
        if 'api_key' in kwargs:
            new_kwargs['api_key'] = kwargs.pop('api_key')
        if 'generate_kraken_signature' in kwargs:
            new_kwargs['generate_kraken_signature'] = kwargs.pop('generate_kraken_signature')
        new_kwargs['options'] = dataclass(**kwargs)

        return func(
            **new_kwargs
        )

    return fn
