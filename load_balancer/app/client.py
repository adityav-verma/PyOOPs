"""Make request to the Load balancer"""
from app.generic_load_balancer import GenericLoadBalancer
from app.generic_server import GenericServer
from app.interfaces.load_balancer_interface import LoadBalancerInterface
from app.interfaces.server_interface import ServerInterface
from app.load_balancer_factory import LoadBalancerFactory
from app.load_balancing_strategy_factory import LoadBalancingStrategyFactory
from app.round_robin_balancing_strategy import RoundRobinBalancingStrategy
from app.server_factory import ServerFactory
from app.success_factor_balancing_strategy import SuccessFactorBalancingStrategy


class Client:
    def __init__(self):
        self._lb = None

    def serve(self, request_id):
        try:
            return self._lb.serve(request_id)
        except Exception as e:
            return str(e)

    def add_sever(self, server: ServerInterface):
        self._lb.add_server(server)

    def add_lb(self, lb: LoadBalancerInterface):
        self._lb = lb


if __name__ == '__main__':
    client = Client()
    lb_factory = LoadBalancerFactory()
    strategy_factory = LoadBalancingStrategyFactory()
    server_factory = ServerFactory()

    client.add_lb(
        lb_factory.create_generic_load_balancer(
            strategy_factory.create_success_percentage_strategy()
        )
    )

    s1 = server_factory.create_generic_server(100, 2, 's1')
    s2 = server_factory.create_generic_server(90, 4, 's2')
    s3 = server_factory.create_generic_server(45, 3, 's3')

    # Should not serve any requests
    for i in range(5):
        print(client.serve(str(i)))

    print('#### Add server S3, should sever all requests ###')

    client.add_sever(s3)
    for i in range(30):
        print(client.serve(str(i)))

    print('#### Add server S1, S1 will be prioritized ###')

    client.add_sever(s1)
    for i in range(11):
        print(client.serve(str(i)))

    print('#### Add server S2, S1 and S2 will get priority over S3 ###')

    client.add_sever(s2)
    for i in range(50):
        print(client.serve(str(i)))

    print('#### Update factor of S1, S1 should get less requests ###')

    s1.factor = 1

    for i in range(100):
        print(client.serve(str(i)))
