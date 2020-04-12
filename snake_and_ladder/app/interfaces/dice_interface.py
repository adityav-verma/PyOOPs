from abc import abstractmethod, ABC


class DiceInterface(ABC):
    @abstractmethod
    def roll(self) -> int:
        """Roll a dice(s) and return the final value"""
        pass
