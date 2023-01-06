from bittrade_kraken_rest import get_server_time, GetServerTimeResult, map_to_result

def test_get_server_time():
    result = get_server_time().pipe(
        map_to_result(result_class=GetServerTimeResult)
    ).run()

    assert result