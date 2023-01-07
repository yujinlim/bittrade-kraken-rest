from reactivex import operators

from bittrade_kraken_rest import get_account_balance_request, get_account_balance_result

from .sign import sign


def test_get_account_balance():
    result = (
        get_account_balance_request()
        .pipe(operators.map(sign), get_account_balance_result())
        .run()
    )
    assert type(result) == dict
