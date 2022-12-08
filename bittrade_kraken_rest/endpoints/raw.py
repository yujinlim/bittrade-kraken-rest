import json

from bittrade_kraken_rest.connection import send_request
from bittrade_kraken_rest.environment.decorators import pretty_print


@pretty_print
def raw(api_key, url, method, json_data=''):
    return send_request(api_key=api_key, url=url, method=method, data=json_data or {})