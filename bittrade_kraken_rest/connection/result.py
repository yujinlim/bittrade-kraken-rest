from reactivex import operators, Observable
from typing import TYPE_CHECKING, TypeVar, Callable
from requests import Response

if TYPE_CHECKING:
    from pydantic.dataclasses import Dataclass


_T = TypeVar("_T", bound='Dataclass')

def map_to_result(result_class: _T) -> Callable[[Observable[Response]], Observable[_T]]:
    return operators.map(lambda x: result_class(**x.json()['result']))

__all__ = [
    "map_to_result",
]
