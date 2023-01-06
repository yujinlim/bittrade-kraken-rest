from pydantic.dataclasses import dataclass


@dataclass
class GetWebsocketsTokenResult:
    expires: int
    token: str
