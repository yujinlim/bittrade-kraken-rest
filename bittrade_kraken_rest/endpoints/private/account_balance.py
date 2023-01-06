from bittrade_kraken_rest.connection.observable import prepare_private


def get_account_balance():
    """
    Get account balances
    :return:
    """
    return prepare_private(url="/0/private/Balance")
