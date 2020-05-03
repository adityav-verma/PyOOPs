from abc import ABC, abstractmethod
from typing import List, Iterator

from app.interfaces.server_interface import ServerInterface

# TODO: Add a factory to build LB


class LoadBalancerInterface(ABC):
    @abstractmethod
    def add_server(self, server: ServerInterface) -> bool: pass

    @abstractmethod
    def remove_server(self, server: ServerInterface) -> bool: pass

    @abstractmethod
    def serve(self, request_id: str) -> dict: pass

    @property
    @abstractmethod
    def servers(self) -> Iterator[ServerInterface]: pass



