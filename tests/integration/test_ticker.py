from bittrade_kraken_rest import ticker, TickerResult, TickerResultEntry


def test_get_server_time():
    result = ticker('USDTUSD').run()

    assert result['USDTZUSD']
