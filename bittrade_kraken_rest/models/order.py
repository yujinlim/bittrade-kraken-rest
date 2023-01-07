from decimal import Decimal
from typing import Any

from pydantic.dataclasses import dataclass


@dataclass
class Order:
    refid: str
    userref: str
    status: str
    opentm: int
    starttm: int
    expiretm: int
    descr: dict[str, Any]
    vol: Decimal
    vol_exec: Decimal
    cost: Decimal
    fee: str
    price: Decimal
    stopprice: str
    limitprice: str
    trigger: str
    misc: str
    oflags: str
    trades: list[Any]
