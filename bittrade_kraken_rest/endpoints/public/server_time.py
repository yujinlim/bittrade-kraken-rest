import requests

from bittrade_kraken_rest.connection import send_public
from bittrade_kraken_rest.models.public.get_server_time import GetServerTimeResult


def get_server_time() -> GetServerTimeResult:
    return send_public(
        url='/0/public/Time',
        result_class=GetServerTimeResult
    )
