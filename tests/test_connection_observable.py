import pytest
from unittest.mock import MagicMock
from unittest.mock import patch
from bittrade_kraken_rest.connection.observable import send_public
import responses

@responses.activate
def test_connection_observable_request_ok():
    responses.add(
        responses.GET,
        "https://api.kraken.com/0/ServerTime",
        json={"error": [], "result": {"a": "b"}},
        status=200,
    )
    asserted = False
    def assertion(value: responses.Response):
        nonlocal asserted
        asserted = True
        assert value.ok
        assert value.json() == {'error': [], 'result': {'a': 'b'}}

    send_public('/0/ServerTime').subscribe(assertion)
    assert asserted