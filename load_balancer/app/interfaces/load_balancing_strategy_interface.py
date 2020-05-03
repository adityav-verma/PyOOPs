from abc import ABC, abstractmethod

from app.interfaces.load_balancer_interface import LoadBalancerInterface
from app.interfaces.server_interface import ServerInterface


class LoadBalancingStrategyInterface(ABC):
    @abstractmethod
    def select_sever(self, load_balancer: LoadBalancerInterface) -> ServerInterface: pass
