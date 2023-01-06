from bittrade_kraken_rest import GetServerTimeResult, get_server_time, map_to_result


def test_get_server_time():
    result = get_server_time().run()

    assert result
