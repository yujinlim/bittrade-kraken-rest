import time
from reactivex import operators

from bittrade_kraken_rest import get_trade_history_request, get_trade_history_result, GetTradeHistoryOptions, GetTradeHistoryResult

from .sign import sign


def test_get_trade_history():
    now = int(time.time())
    options = GetTradeHistoryOptions(
        end=now
    )
    result = (
        get_trade_history_request(options)
        .pipe(operators.map(sign), get_trade_history_result())
        .run()
    )
    assert type(result) == GetTradeHistoryResult
