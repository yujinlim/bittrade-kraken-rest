from typing import Literal
import requests

from bittrade_kraken_rest.connection.nonce import get_nonce
from bittrade_kraken_rest.connection.signature import get_kraken_signature

API_URL = 'https://api.kraken.com'


def send_request(*, api_key: str, url: str, method: Literal['get', 'post'], data=None) -> requests.Response:
    """Send request to Kraken REST API

      Args:
          api_key (str): api key
          secret (str): secret
          url (str): should start with a "/" or include the full kraken api domain (so you may use beta apis)
          method (get|post): http method
          data (dict): Data to be sent to kraken

      Returns:
          _type_: _description_
    """
    data = dict(
        nonce=get_nonce(),
        **(data or {})
    )
    headers = {
        'API-Key': api_key,
        'API-Sign': get_kraken_signature(url, data),
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
    }
    if not url.startswith(API_URL):
        url = f'{API_URL}{url}'
    return getattr(requests, method.lower())(
        url,
        data=data,
        headers=headers
    )


