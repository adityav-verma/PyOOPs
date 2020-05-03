from app.interfaces.load_balancer_interface import LoadBalancerInterface
from app.interfaces.load_balancing_strategy_interface import LoadBalancingStrategyInterface
from app.interfaces.server_interface import ServerInterface


class SuccessFactorBalancingStrategy(LoadBalancingStrategyInterface):
    # O(n) time | O(n) space
    def select_sever(self, load_balancer: LoadBalancerInterface) -> ServerInterface:
        # TODO: Maybe strategy should hold the servers
        candidate_server, success_percentage = None, float('-inf')

        for server in load_balancer.servers:
            if server.current_requests < server.max_request_limit:
                if server.factor > success_percentage:
                    success_percentage = server.factor
                    candidate_server = server
        if not candidate_server:
            raise Exception('No severs available')
        return candidate_server
