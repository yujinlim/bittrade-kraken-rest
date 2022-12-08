import requests

from bittrade_kraken_rest.connection import send_request


def get_server_time():
    return send_request(
        url='/0/public/Time',
        method='get',
    )