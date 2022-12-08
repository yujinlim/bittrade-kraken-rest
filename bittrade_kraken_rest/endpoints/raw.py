import json

from bittrade_kraken_rest.connection import send_request


def raw(api_key, url, method, json_data=''):
    return send_request(api_key=api_key, url=url, method=method, data=json_data or {})