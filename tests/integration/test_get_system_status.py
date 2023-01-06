from bittrade_kraken_rest import get_system_status
from datetime import datetime


def test_get_system_status():
    result = get_system_status().run()

    assert result.status
    assert type(result.timestamp) == datetime
