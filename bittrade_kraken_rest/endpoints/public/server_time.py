import requests

from bittrade_kraken_rest.connection import send_public
from bittrade_kraken_rest.models.public.get_server_time import GetServerTimeResult
from returns.result import Success
from returns.io import IOResultE


def get_server_time() -> IOResultE[GetServerTimeResult]:
    return send_public(
        url='/0/public/Time'
    ).bind_result(
        lambda x: Success(GetServerTimeResult(**x))
    )
