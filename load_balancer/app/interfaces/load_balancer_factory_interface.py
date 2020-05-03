from abc import abstractmethod, ABC

from app.generic_load_balancer import GenericLoadBalancer
from app.interfaces.load_balancing_strategy_interface import LoadBalancingStrategyInterface


class LoadBalancerFactoryInterface(ABC):
    @abstractmethod
    def create_generic_load_balancer(self, strategy: LoadBalancingStrategyInterface) -> GenericLoadBalancer: pass