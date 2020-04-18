import unittest
from unittest import mock

from app import App
from app.board_factory import BoardFactory
from app.board_list_factory import BoardListFactory
from app.card_factory import CardFactory
from app.interfaces.app_interface import AppInterface
from app.constants import BoardPrivacyType


class TestAppCreation(unittest.TestCase):
    def test_app_creation(self):
        app = App(BoardFactory(), BoardListFactory(), CardFactory())
        self.assertIsInstance(app, AppInterface)


class TestAppFunc(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App(BoardFactory(), BoardListFactory(), CardFactory())

    # @mock.patch.object(App, 'board_factory')
    def test_create_board(self):
        name = 'test board'
        privacy = BoardPrivacyType.PUBLIC
        response = self.app.create_board(name, privacy)
        self.assertIsInstance(response, str)
        self.assertEqual(len(self.app.boards), 1)

    def test_create_list(self):
        name = 'test name'
        board_id = self.app.create_board('test board', BoardPrivacyType.PUBLIC)
        response = self.app.create_list(name, board_id)
        self.assertIsInstance(response, str)
        self.assertEqual(len(self.app.boards[0].lists), 1)

    def test_create_card(self):
        name = 'test name'
        board_id = self.app.create_board('test board', BoardPrivacyType.PUBLIC)
        list_id = self.app.create_list(name, board_id)
        response = self.app.create_card('card', 'description', list_id)
        self.assertIsInstance(response, str)
        self.assertEqual(len(self.app.boards[0].lists[0].cards), 1)