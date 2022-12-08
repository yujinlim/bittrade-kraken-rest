from bittrade_kraken_rest.connection import send_request
from bittrade_kraken_rest.connection.signature import KrakenSignatureBuilder
from bittrade_kraken_rest.environment.decorators import with_api_key, to_result
from bittrade_kraken_rest.models.private.get_account_balance import GetAccountBalanceResult


@with_api_key
def get_account_balance(*, api_key: str = '', generate_kraken_signature: KrakenSignatureBuilder = None):
    """
    Get account balances
    :param generate_kraken_signature: Optional[KrakenSignatureBuilder] The method used to generate the signature.
    :param api_key:
    :return:
    """
    return send_request(
        api_key=api_key,
        url='/0/private/Balance',
        method='post',
        generate_kraken_signature=generate_kraken_signature,
    )


get_account_balance_result = to_result(GetAccountBalanceResult, get_account_balance)
