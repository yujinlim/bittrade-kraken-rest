import dataclasses
from typing import Literal


@dataclasses.dataclass
class CancelAllEvent:
    event = "cancelAll"

@dataclasses.dataclass
class CancelAllResult:
    count: int = 0
    event = "cancelAllStatus"
    status: str = Literal["ok", "error"]