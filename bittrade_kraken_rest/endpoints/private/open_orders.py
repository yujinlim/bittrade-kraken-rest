import dataclasses

from bittrade_kraken_rest.connection.observable import prepare_private
from bittrade_kraken_rest.models.private.get_open_orders import (
    GetOpenOrdersOptions,
    GetOpenOrdersResult,
)


def get_open_orders(*, options: GetOpenOrdersOptions = None):
    """
    Get open orders
    :param options: GetOpenOrdersOptions
    :return:
    """
    options = options or GetOpenOrdersOptions()
    return prepare_private(
        url="/0/private/OpenOrders",
        data=dataclasses.asdict(options),
    )
