import inspect
import json
from typing import Dict

import fire
from rich.console import Console
from rich.table import Table

from bittrade_kraken_rest import (
    get_account_balance,
    get_open_orders,
    get_server_time,
    get_system_status,
)
from bittrade_kraken_rest.endpoints.raw import raw
from bittrade_kraken_rest.environment.cli import pretty_print, private, kwargs_to_options
from bittrade_kraken_rest.models.private.get_open_orders import GetOpenOrdersOptions


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
        console = Console()
        while command := console.input('Type endpoint name: [italic]use ? for a list, q to quit[/italic]\n'):
            if command == 'q':
                return
            if command == '?':
                table = Table('Endpoint', 'Description')

            else:
                func = getattr(Cli, command)
                signature = inspect.signature(func)
                if 'data' in signature.parameters:
                    options = json.loads(
                        console.input('Options (json string) ').strip("'")
                    )

                    func(data=options)
                else:
                    func()
                console.line(2)

    @staticmethod
    def get_account_balance():
        return private(
            pretty_print(get_account_balance))()

    @staticmethod
    def get_server_time():
        return pretty_print(get_server_time)()

    @staticmethod
    def get_system_status():
        return pretty_print(get_system_status)()

    @staticmethod
    def raw():
        return pretty_print(raw)


if __name__ == '__main__':
    fire.Fire(Cli)
