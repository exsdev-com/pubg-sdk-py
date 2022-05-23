"""PUBG API endpoints."""

from typing import TYPE_CHECKING, Any

from .helpers import pick
from .typing import SyncAsync

if TYPE_CHECKING:
    from .client import BaseClient


class Endpoint:
    def __init__(self, parent: "BaseClient") -> None:
        self.parent = parent


class ShardsEndpoint(Endpoint):
    # raise NotImplementedError("API ERROR: not implemented winner dinner chicken dinner")
    def samples(self, platform: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"shards/{platform}/samples",
            method="GET",
            # query=pick(kwargs, "start_cursor", "page_size"),
            auth=kwargs.get("auth"),
        )