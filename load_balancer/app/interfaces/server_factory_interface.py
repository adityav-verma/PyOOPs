from abc import abstractmethod, ABC
from typing import Optional

from app.generic_server import GenericServer


class ServerFactoryInterface(ABC):
    @abstractmethod
    def create_generic_server(self, factor: int, max_requests: int, id: Optional[str] = None) -> GenericServer: pass
