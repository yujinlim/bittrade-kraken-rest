from reactivex import operators

from bittrade_kraken_rest import cancel_all_request, cancel_all_result, CancelAllResult

from .sign import sign


def test_get_account_balance():
    result = (
        cancel_all_request()
        .pipe(operators.map(sign), cancel_all_result())
        .run()
    )
    assert type(result) == CancelAllResult
