import unittest

from app.factories.board_factory import BoardFactory


class TestBoardFactory(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_board(self):
        """Create a new board, with the given size"""
        size = 10
        board = BoardFactory.create_board(size)
        self.assertEqual(board.size, size)
