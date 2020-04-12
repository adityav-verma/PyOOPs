from abc import ABC, abstractmethod

from app.interfaces.dice_interface import DiceInterface


class DiceFactoryInterface(ABC):
    @staticmethod
    @abstractmethod
    def get_dice() -> DiceInterface:
        """Return a singular dice"""
        pass

    @staticmethod
    @abstractmethod
    def get_composite_dice(count: int) -> DiceInterface:
        """Return a composite dice holding count number of dices"""
        pass
