import dataclasses


@dataclasses.dataclass
class GetWebsocketsTokenResult:
    expires: int
    token: str
