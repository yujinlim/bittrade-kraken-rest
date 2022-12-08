from bittrade_kraken_rest.connection import send_request
from bittrade_kraken_rest.environment.decorators import with_api_key, pretty_print


@with_api_key
def get_account_balance(api_key: str = ''):
    """
    Get account balances
    :param api_key:
    :return:
    """
    return send_request(
        api_key=api_key,
        url='/0/private/Balance',
        method='post'
    )
