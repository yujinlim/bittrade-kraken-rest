from typing import Callable, Dict
import importlib
from os import getenv
from rich.console import Console

KrakenSignatureBuilder = Callable[[Dict], str]

get_kraken_signature: KrakenSignatureBuilder


def get_kraken_signature(*args, **kwargs):
    console = Console()
    console.bell()
    console.line()
    console.rule('Kraken signature implementation missing')
    console.print('''
        This library believes in BYOC (Bring Your Own Credentials).
        Implement the signature calculation yourself 
        and export its module path to env [red]KRAKEN_SIGNATURE_MODULE[/red]
        Maybe copy from Kraken's official reference? https://docs.kraken.com/rest/#section/Authentication/Headers-and-Signature
    ''')
    try:
        raise NotImplementedError('You need to implement your own signature method.')
    except NotImplementedError as exc:
        console.print_exception()
        raise exc


try:
    module = importlib.import_module(
        getenv('KRAKEN_SIGNATURE_MODULE', 'bittrade_kraken_rest.connection.signature.generate')
    )
    get_kraken_signature = module.get_kraken_signature
except (ImportError, AttributeError):
    pass
