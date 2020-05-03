from typing import Union

from app.interfaces.load_balancer_interface import LoadBalancerInterface
from app.interfaces.load_balancing_strategy_interface import LoadBalancingStrategyInterface
from app.interfaces.server_interface import ServerInterface


class RoundRobinBalancingStrategy(LoadBalancingStrategyInterface):
    def __init__(self):
        self._last_server: Union[str, None] = None

    def select_sever(self, load_balancer: LoadBalancerInterface) -> ServerInterface:
        if not self._last_server:
            for server in load_balancer.servers:
                if server.current_requests < server.max_request_limit:
                    self._last_server = server.id
                    return server
            raise Exception('No servers availablec')

        search = False
        for server in load_balancer.servers:
            if search:
                if server.current_requests < server.max_request_limit:
                    self._last_server = server.id
                    return server
            if server.id == self._last_server:
                search = True

        for server in load_balancer.servers:
            if server.id == self._last_server:
                break
            else:
                if server.current_requests < server.max_request_limit:
                    self._last_server = server.id
                    return server

        raise Exception('No servers available')
