from reactivex import operators

from bittrade_kraken_rest import (
    GetOpenOrdersResult,
    get_open_orders_request,
    get_open_orders_result,
)

from .sign import sign


def test_get_open_orders():
    result = (
        get_open_orders_request()
        .pipe(operators.map(sign), get_open_orders_result())
        .run()
    )
    assert type(result) == GetOpenOrdersResult
