from bittrade_kraken_rest.models.message import KrakenMessage
from pydantic.dataclasses import dataclass


@dataclass
class GetServerTimeResult:
    unixtime: int
    rfc1123: str

