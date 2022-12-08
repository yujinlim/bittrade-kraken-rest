import inspect
import json
from typing import Dict

import fire
from rich.console import Console
from rich.table import Table

from bittrade_kraken_rest.endpoints.private.get_account_balance import get_account_balance
from bittrade_kraken_rest.endpoints.private.get_open_orders import get_open_orders
from bittrade_kraken_rest.endpoints.public.get_server_time import get_server_time
from bittrade_kraken_rest.endpoints.raw import raw
from bittrade_kraken_rest.environment.cli import pretty_print, private, kwargs_to_options
from bittrade_kraken_rest.models.private.get_open_orders import GetOpenOrdersOptions


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


class Cli:
    @staticmethod
    def get_open_orders(data: Dict = None):
        """

        :param data: Json string in the GetOpenOrdersOptions format; refer https://docs.kraken.com/rest/#tag/User-Data/operation/getOpenOrders
        :return:
        """
        options = data or {}

        return private(
            pretty_print(
                kwargs_to_options(GetOpenOrdersOptions, get_open_orders)
            )
        )(**options)

    @staticmethod
    def interactive():
        return interactive()

    @staticmethod
    def get_account_balance():
        return private(pretty_print(get_account_balance))

    @staticmethod
    def get_server_time():
        return pretty_print(get_server_time)

    @staticmethod
    def raw():
        return pretty_print(raw)


if __name__ == '__main__':
    fire.Fire(Cli)
