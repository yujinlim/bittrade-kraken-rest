from bittrade_kraken_rest.connection import send_public
from bittrade_kraken_rest.models.public.get_system_status import GetSystemStatusResult


def get_system_status() -> GetSystemStatusResult:
    return send_public(url="/0/public/SystemStatus", result_class=GetSystemStatusResult)


__all__ = [
    "get_system_status",
]
