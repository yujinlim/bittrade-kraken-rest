import dataclasses

from bittrade_kraken_rest.connection import send_request, KrakenSignatureBuilder
from bittrade_kraken_rest.environment.decorators import with_api_key, to_result
from bittrade_kraken_rest.models.private.get_open_orders import GetOpenOrdersOptions, GetOpenOrdersResponse, \
    GetOpenOrdersResult


@with_api_key
def get_open_orders(*, api_key: str = '', generate_kraken_signature: KrakenSignatureBuilder = None,
                    options: GetOpenOrdersOptions = None):
    """
    Get open orders
    :param api_key: Api key
    :param generate_kraken_signature: Method to generate signature from url and data
    :param options: GetOpenOrdersOptions
    :return:
    """
    options = options or GetOpenOrdersOptions()
    return send_request(
        api_key=api_key,
        url='/0/private/OpenOrders',
        method='post',
        data=dataclasses.asdict(options),
        generate_kraken_signature=generate_kraken_signature,
    )


get_open_orders_result = to_result(GetOpenOrdersResult, get_open_orders)