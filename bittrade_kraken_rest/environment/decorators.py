from functools import wraps
from os import getenv

import requests
from rich.console import Console

console = Console()


def with_api_key(func):
    @wraps(func)
    def fn(api_key: str = '', *args, **kwargs):
        if not api_key:
            api_key = getenv('KRAKEN_API_KEY')
        if not api_key:
            console.bell()
            console.rule('Missing credentials')
            console.print('''
                API key or secret missing. 
                You should add them to your environment as 
                [red]KRAKEN_API_KEY[/red] and [red]KRAKEN_API_SECRET[/red],
                or pass them as arguments to the CLI
            ''')
            return
        return func(api_key, *args, **kwargs)
    return fn


def pretty_print(func):
    @wraps(func)
    def fn(*args, **kwargs):
        outcome: requests.Response = func(*args, **kwargs)
        console.line()
        if outcome.ok:
            if not outcome.json()['error']:
                style = 'green'
            else:
                style = 'red'
        else:
            style = 'bold red'
        console.rule(outcome.request.url, style=style)
        if outcome.ok:
            console.print_json(outcome.text)
            console.line()
        else:
            console.print(f'Failed with status {outcome.status_code}')
        console.rule('From request:', style='cyan')
        console.print(outcome.request.__dict__)
        console.line(2)

    return fn