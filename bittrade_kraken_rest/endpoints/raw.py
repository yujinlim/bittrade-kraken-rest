import json
from typing import Dict

from bittrade_kraken_rest.connection import send_request


def raw(*, api_key: str='', url: str='', method: str='', options: Dict=None):
    return send_request(api_key=api_key, url=url, method=method, data=options or {})