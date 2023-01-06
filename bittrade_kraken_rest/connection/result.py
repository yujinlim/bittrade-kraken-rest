from typing import TYPE_CHECKING, Any, Callable, Type, TypeVar

from reactivex import Observable, operators
from requests.models import Response
from reactivex import compose

if TYPE_CHECKING:
    from pydantic.dataclasses import Dataclass


_T = TypeVar("_T")
# _T = TypeVar("_T", bound="Dataclass") Need to look into this: All our @dataclass are not compatible with Dataclass


def map_to_result(
    result_class: Type[_T],
) -> Callable[[Observable[Response]], Observable[_T]]:
    def to_json(x: Response) -> dict[str, Any]:
        return x.json()

    return compose(
        operators.map(to_json),
        operators.map(lambda x: x["result"]),
        operators.map(lambda x: result_class(**x)),
    )


__all__ = [
    "map_to_result",
]
