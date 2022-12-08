import inspect
import fire
from rich.console import Console
from rich.table import Table

from bittrade_kraken_rest.endpoints.private.get_account_balance import get_account_balance
from bittrade_kraken_rest.endpoints.raw import raw
from bittrade_kraken_rest.environment.decorators import pretty_print


def interactive():
    console = Console()
    while command := console.input('Type command: [italic]use ? for a list, q to quit[/italic]\n'):
        if command == 'q':
            return
        if command == '?':
            _help(console)
        else:
            args = []
            func = methods[command]
            for arg_name in inspect.getfullargspec(methods[command]).args:
                args.append(console.input(f'Value for {arg_name}'))
            func(*args)


def _help(console):
    """
    List down options
    :return:
    """
    keys = list(methods.keys())
    keys.sort()
    table = Table()
    table.add_column('Name')
    table.add_column('Doc')
    for name in keys:
        func = methods[name]
        table.add_row(name, func.__doc__)
    console.print(table)


methods = {
    "get_account_balance": pretty_print(get_account_balance),
    "raw": pretty_print(raw),
    "interactive": interactive,
}

if __name__ == '__main__':
    fire.Fire(methods)
