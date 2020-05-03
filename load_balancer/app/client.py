"""Make request to the Load balancer"""
from app.generic_load_balancer import GenericLoadBalancer
from app.generic_server import GenericServer
from app.interfaces.server_interface import ServerInterface
from app.success_factor_balancing_strategy import SuccessFactorBalancingStrategy


class Client:
    def __init__(self):
        self._lb = GenericLoadBalancer(SuccessFactorBalancingStrategy())

    def serve(self, request_id):
        try:
            return self._lb.serve(request_id)
        except Exception as e:
            return str(e)

    def add_sever(self, server: ServerInterface):
        self._lb.add_server(server)


if __name__ == '__main__':
    client = Client()

    s1 = GenericServer(2, 100, 's1')
    s2 = GenericServer(4, 90, 's2')
    s3 = GenericServer(7, 45, 's3')

    # Should not serve any requests
    for i in range(5):
        print(client.serve(str(i)))

    print('#### Add server ###')

    client.add_sever(s3)
    for i in range(10):
        print(client.serve(str(i)))

    print('#### Add server ###')

    client.add_sever(s1)
    for i in range(11):
        print(client.serve(str(i)))

    print('#### Add server ###')

    client.add_sever(s2)
    for i in range(50):
        print(client.serve(str(i)))
