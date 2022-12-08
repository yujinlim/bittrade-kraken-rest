import requests

from bittrade_kraken_rest.connection import send_request
from bittrade_kraken_rest.environment.decorators import to_result
from bittrade_kraken_rest.models.public.get_system_status import GetSystemStatusResult


def get_system_status():
    return send_request(
        url='/0/public/SystemStatus',
        method='get',
    )


get_system_status_result = to_result(GetSystemStatusResult, get_system_status)
