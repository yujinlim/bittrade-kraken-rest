from typing import Dict

from ..message import KrakenMessage
import dataclasses



@dataclasses.dataclass
class GetAccountBalanceResponse(KrakenMessage):
    result: Dict[str, str]
