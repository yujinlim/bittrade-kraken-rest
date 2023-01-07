from bittrade_kraken_rest import get_server_time


def test_get_server_time():
    result = get_server_time().run()

    assert result
