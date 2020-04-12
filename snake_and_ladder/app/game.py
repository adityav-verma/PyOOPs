"""Facade, which provides high level APIs for a game"""
import random
from typing import List

from app.board import Board
from app.factories.box_factory import BoxFactory
from app.factories.dice_factory import DiceFactory
from app.interfaces.board_interface import BoardInterface
from app.interfaces.game_interface import GameInterface
from app.interfaces.move_interface import MoveInterface
from app.interfaces.player_interface import PlayerInterface
from app.move import Move
from app.player import Player


class Game(GameInterface):
    def __init__(self):
        self._board: BoardInterface = Board(100, BoxFactory)
        self._players: List[PlayerInterface] = []
        self._winner: PlayerInterface = None
        self._current_player_index: int = 0
        self._moves: List[MoveInterface] = []
        self._dice = DiceFactory.get_composite_dice(2)

    def reset(self) -> None:
        self.board.reset()
        self._moves = []
        self._winner = None
        self._current_player_index = 0
        for player in self._players:
            player.current_box = self.board.get_box(0)

    @property
    def board(self):
        return self._board

    @property
    def moves(self) -> List[MoveInterface]:
        return self._moves

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
            print('Cannot start game, please add at-least 2 players and try again!')
            return

        current_player = self._players[0]
        while not self._winner:
            print(f'Current {current_player}')
            dice_value = self._dice.roll()
            move = Move(self, current_player, dice_value)
            move.invoke()
            self._moves.append(move)
            if current_player.current_box.position == 100:
                self._winner = current_player
            current_player = self._get_next_player(current_player)
            print('-------------')
        print(f'{self._winner} won the game')