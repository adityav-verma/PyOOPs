from typing import Optional

from app.generic_server import GenericServer
from app.interfaces.server_factory_interface import ServerFactoryInterface
from app.interfaces.server_interface import ServerInterface


class ServerFactory(ServerFactoryInterface):
    def create_generic_server(self, factor: int, max_requests: int, id: Optional[str] = None) -> GenericServer:
        return GenericServer(max_requests, factor, id)
