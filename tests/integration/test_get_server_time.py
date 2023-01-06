from bittrade_kraken_rest import get_server_time
from returns.unsafe import unsafe_perform_io

def test_get_server_time():
    result = get_server_time()
    unsafe_perform_io(result)