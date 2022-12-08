from typing import Literal, Optional
import requests

from bittrade_kraken_rest.connection.nonce import get_nonce
from bittrade_kraken_rest.connection.signature import KrakenSignatureBuilder

API_URL = 'https://api.kraken.com'


def send_request(*, url: str, method: Literal['get', 'post'], api_key: str='', data=None, generate_kraken_signature: Optional[KrakenSignatureBuilder]=None) -> requests.Response:
    """Send request to Kraken REST API

      Args:
          api_key (str): api key
          secret (str): secret
          url (str): should start with a "/" or include the full kraken api domain (so you may use beta apis)
          method (get|post): http method
          data (dict): Data to be sent to kraken
          generate_api_key: method that accepts a url and data dictionary and returns

      Returns:
          _type_: _description_
    """
    data = dict(
        nonce=get_nonce(),
        **(data or {})
    )
    if 'private' in url:
        if not generate_kraken_signature:
            raise NotImplementedError('You need to implement generate_kraken_signature for private urls')
        headers = {
            'API-Key': api_key,
            'API-Sign': generate_kraken_signature(url, data),
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
        }
    else:
        headers = {
            'Content-Type': 'application/json'
        }



    if not url.startswith(API_URL):
        url = f'{API_URL}{url}'
    return getattr(requests, method.lower())(
        url,
        data=data,
        headers=headers
    )


