from decimal import Decimal
from pydantic.dataclasses import dataclass
from typing import Dict, List


@dataclass
class Order:
    refid: str
    userref: str
    status: str
    opentm: int
    starttm: int
    expiretm: int
    descr: Dict
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
    trades: List
