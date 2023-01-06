from bittrade_kraken_rest.connection import send_private


def get_account_balance():
    """
    Get account balances
    :return:
    """
    return send_private(url="/0/private/Balance", result_class=dict)
