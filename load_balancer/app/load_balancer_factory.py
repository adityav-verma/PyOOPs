from app.generic_load_balancer import GenericLoadBalancer
from app.interfaces.load_balancer_factory_interface import LoadBalancerFactoryInterface
from app.interfaces.load_balancing_strategy_interface import LoadBalancingStrategyInterface


class LoadBalancerFactory(LoadBalancerFactoryInterface):

    def create_generic_load_balancer(self, strategy: LoadBalancingStrategyInterface) -> GenericLoadBalancer:
        return GenericLoadBalancer(strategy)
