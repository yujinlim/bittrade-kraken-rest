import dataclasses
from typing import Dict

from ..message import KrakenMessage

GetAccountBalanceResult = dict[str, str]


@dataclasses.dataclass
class GetAccountBalanceResponse(KrakenMessage):
    result: GetAccountBalanceResult
