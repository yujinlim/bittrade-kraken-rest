import pytest
from unittest.mock import MagicMock
from unittest.mock import patch
from bittrade_kraken_rest.connection.observable import send_public
import responses
import requests

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


@responses.activate
def test_connection_observable_request_error():
    responses.add(
        responses.GET,
        "https://api.kraken.com/0/ServerTime",
        json={"error": [], "result": {"a": "b"}},
        status=400,
    )
    asserted = False
    def assertion(error):
        nonlocal asserted
        asserted = True
        assert type(error) == requests.HTTPError
        assert str(error).startswith('400')

    send_public('/0/ServerTime').subscribe(on_error=assertion)
    assert asserted

@responses.activate
def test_connection_observable_request_kraken_error():
    responses.add(
        responses.GET,
        "https://api.kraken.com/0/ServerTime",
        json={"error": ["Not cool"]},
        status=200,
    )
    asserted = False
    def assertion(error):
        nonlocal asserted
        asserted = True
        assert type(error) == Exception
        assert str(error) == 'Not cool'

    send_public('/0/ServerTime').subscribe(on_error=assertion)
    assert asserted