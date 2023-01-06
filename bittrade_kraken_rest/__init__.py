from .endpoints.public.server_time import GetServerTimeResult, get_server_time
from .endpoints.public.system_status import GetSystemStatusResult, get_system_status
from .connection.result import map_to_result

__version__ = "0.11.0"

__all__ = [
    "__version__",
    "get_server_time",
    "get_system_status",
    "GetServerTimeResult",
    "GetSystemStatusResult",
    "map_to_result",
]
