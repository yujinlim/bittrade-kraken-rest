from bittrade_kraken_rest.connection.observable import send_public
from pydantic.dataclasses import dataclass
import requests
from reactivex import Observable


@dataclass
class GetServerTimeResult:
    unixtime: int
    rfc1123: str

def get_server_time() -> Observable[requests.Response]:
    return send_public(
        url='/0/public/Time'
    )
