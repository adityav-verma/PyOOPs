import random
from typing import List

from app.interfaces.dice_interface import DiceInterface


class Dice(DiceInterface):
    def roll(self) -> int:
        value = random.randint(1, 6)
        print(f'Dice roll gave {value}')
        return value


class CompositeDice(list, DiceInterface):
    def __init__(self, dices: List[DiceInterface] = []):
        for dice in dices:
            self.append(dice)

    def roll(self) -> int:
        value = 0
        for dice in self:
            value += dice.roll()
        print(f'Dice roll gave {value}')
        return value
