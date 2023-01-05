from bittrade_kraken_rest.models.request import _get_result
from returns.result import Success, Failure
import pytest


def test_get_result():
    response_json = {
        "error": [ ],
        "result": [
        {
        "id": "VSKC",
        "descr": "my_trades_1",
        "format": "CSV",
        "report": "trades",
        "subtype": "all",
        "status": "Processed"
        }]}

    assert _get_result(response_json) == Success([
        {
        "id": "VSKC",
        "descr": "my_trades_1",
        "format": "CSV",
        "report": "trades",
        "subtype": "all",
        "status": "Processed"
        }])

def test_get_result_error():
    response_json = {
  "error": [
    "EGeneral:Invalid arguments"
  ]
}
    result = _get_result(response_json).failure()
    assert type(result) == Exception
    assert str(result) == "EGeneral:Invalid arguments"
