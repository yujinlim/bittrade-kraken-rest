import requests

from bittrade_kraken_rest.connection import send_request
from bittrade_kraken_rest.environment.decorators import to_result
from bittrade_kraken_rest.models.public.get_server_time import GetServerTimeResult


def get_server_time():
    return send_request(
        url='/0/public/Time',
        method='get',
    )


get_server_time_result = to_result(GetServerTimeResult, get_server_time)
