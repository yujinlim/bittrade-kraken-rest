from reactivex import operators

from bittrade_kraken_rest import (
    get_websockets_token_request,
    get_websockets_token_result,
)

from .sign import sign


def test_get_open_orders():
    result = (
        get_websockets_token_request()
        .pipe(operators.map(sign), get_websockets_token_result())
        .run()
    )
    assert result.token
