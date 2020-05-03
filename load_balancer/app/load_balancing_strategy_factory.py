from app.interfaces.load_balancing_strategy_factory_interface import LoadBalancingStrategyFactoryInterface
from app.round_robin_balancing_strategy import RoundRobinBalancingStrategy
from app.success_factor_balancing_strategy import SuccessFactorBalancingStrategy


class LoadBalancingStrategyFactory(LoadBalancingStrategyFactoryInterface):
    def create_round_robin_strategy(self) -> RoundRobinBalancingStrategy:
        return RoundRobinBalancingStrategy()

    def create_success_percentage_strategy(self) -> SuccessFactorBalancingStrategy:
        return SuccessFactorBalancingStrategy()