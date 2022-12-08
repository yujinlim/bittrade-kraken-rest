import fire
from rich.console import Console
from rich.table import  Table

from bittrade_kraken_rest.endpoints.private.get_account_balance import get_account_balance
from bittrade_kraken_rest.endpoints.raw import raw


def interactive():
    console = Console()
    while command := console.input('Type command: [italic]use ? for a list, q to quit[/italic]\n'):
        if command == '?':
            help(console)
        if command == 'q':
            return

def help(console):
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
    "get_account_balance": get_account_balance,
    "raw": raw,
    "interactive": interactive,
}

if __name__ == '__main__':
    fire.Fire(methods)