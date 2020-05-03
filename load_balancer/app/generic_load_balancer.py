from typing import Dict, List

from app.interfaces.load_balancer_interface import LoadBalancerInterface
from app.interfaces.load_balancing_strategy_interface import LoadBalancingStrategyInterface
from app.interfaces.server_interface import ServerInterface


class GenericLoadBalancer(LoadBalancerInterface):

    def __init__(self, load_balancing_strategy: LoadBalancingStrategyInterface):
        self._strategy = load_balancing_strategy
        self._servers: Dict[str, ServerInterface] = {}

    def _cleanup(self):
        for server_id, server in self._servers.items():
            server.clean_severed_requests()

    @property
    def servers(self) -> List[ServerInterface]:
        for _, server in self._servers.items():
            yield server

    def add_server(self, server: ServerInterface) -> bool:
        if server.id in self._servers:
            return True
        self._servers[server.id] = server
        return True

    def remove_server(self, server: ServerInterface) -> bool:
        if server.id not in self._servers:
            return True
        self._servers.pop(server.id)
        return True

    def serve(self, request_id: str) -> dict:
        # Ideally this should be an async function
        self._cleanup()
        server = self._strategy.select_sever(self)
        server.serve(request_id)
        return {'request_id': request_id, 'server_id': server.id}