import requests
from pydantic.dataclasses import dataclass
from reactivex import Observable

from bittrade_kraken_rest.connection.observable import send_public


@dataclass
class GetServerTimeResult:
    unixtime: int
    rfc1123: str


def get_server_time() -> Observable[requests.Response]:
    return send_public(url="/0/public/Time")


__all__ = [
    "GetServerTimeResult",
    "get_server_time",
]
