from app.dice import Dice, CompositeDice
from app.interfaces.dice_factory_interface import DiceFactoryInterface
from app.interfaces.dice_interface import DiceInterface


class DiceFactory(DiceFactoryInterface):
    @staticmethod
    def get_dice() -> DiceInterface:
        return Dice()

    @staticmethod
    def get_composite_dice(count: int) -> DiceInterface:
        dices = [Dice() for _ in range(count)]
        return CompositeDice(dices)
