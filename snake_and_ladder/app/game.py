"""Facade, which provides high level APIs for a game"""
import random
from typing import List

from app.board import Board
from app.interfaces.board_interface import BoardInterface
from app.interfaces.game_interface import GameInterface
from app.interfaces.move_interface import MoveInterface
from app.interfaces.player_interface import PlayerInterface
from app.move import Move
from app.player import Player


# TODO: move to an external implementation, composite pattern maybe
def roll_dice():
    return random.randint(1, 6)


class Game(GameInterface):
    def __init__(self):
        self._board: BoardInterface = Board(100)
        self._players: List[PlayerInterface] = []
        self._winner: PlayerInterface = None
        self._current_player_index: int = 0
        self._moves: List[MoveInterface] = []

    @property
    def board(self):
        return self._board

    def _get_next_player(self, curr_player_index):
        curr_player_index = self._players.index(curr_player_index) + 1
        curr_player_index = curr_player_index % len(self._players)
        return self._players[curr_player_index]

    def add_player(self, name):
        player = Player(name)
        player.current_box = self.board.get_box(0)
        self._players.append(player)

    def add_snake(self, start, end):
        self._board.add_snake(start, end)

    def add_ladder(self, start, end):
        self._board.add_ladder(start, end)

    def start_game(self):
        if len(self._players) < 2:
            print('Cannot start game without players, please add at-least 2 and try again!')

        current_player = self._players[0]
        while not self._winner:
            dice_value = roll_dice()
            print(f'{current_player} rolled a dice for value {dice_value}')
            move = Move(self, current_player, dice_value)
            move.invoke()
            print(f'{current_player}')
            if current_player.current_box.position == 100:
                self._winner = current_player
            current_player = self._get_next_player(current_player)
        print(f'{self._winner} won the game')