from app.interfaces.game_interface import GameInterface
from app.interfaces.move_interface import MoveInterface
from app.interfaces.player_interface import PlayerInterface


class Move(MoveInterface):
    def __init__(self, game: GameInterface, player: PlayerInterface, steps: int):
        self.player = player
        self.steps = steps
        self.game = game
        self.board = game.board
        self.success = None

    def invoke(self):
        next_box_index = self.player.current_box.position + self.steps
        try:
            current_box = self.player.current_box
            while current_box != self.game.board.get_box(next_box_index):
                current_box = self.game.board.get_box(next_box_index)
                next_box_index = current_box.next_position()
            self.player.current_box = current_box
        except Exception:
            print(f'Player: {self.player} cannot move {self.steps} steps, skipping')
            self.success = False
            return

    def undo(self):
        pass
