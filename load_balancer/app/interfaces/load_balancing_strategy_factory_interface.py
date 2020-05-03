from abc import abstractmethod, ABC

from app.round_robin_balancing_strategy import RoundRobinBalancingStrategy
from app.success_factor_balancing_strategy import SuccessFactorBalancingStrategy


class LoadBalancingStrategyFactoryInterface(ABC):
    @abstractmethod
    def create_success_percentage_strategy(self) -> SuccessFactorBalancingStrategy: pass

    @abstractmethod
    def create_round_robin_strategy(self) -> RoundRobinBalancingStrategy: pass
