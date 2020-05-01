import unittest

from app.constants import BoardPrivacy
from app.trello import Trello


class TestBoardLists(unittest.TestCase):
    def setUp(self) -> None:
        self.api = Trello()
        self.board_id = self.api.create_board('Test Board', BoardPrivacy.PUBLIC)

    def test_create_list(self):
        name = 'test list'
        list_id = self.api.create_list(name, self.board_id)
        self.assertIsInstance(list_id, str)

        show_list = {'id': list_id, 'name': name, 'cards': []}

        show_list_response = self.api.show_list(list_id)
        self.assertEqual(show_list, show_list_response)

    def test_show_list(self):
        name = 'test list'
        list_id = self.api.create_list(name, self.board_id)
        self.assertIsInstance(list_id, str)

        show_list = {'id': list_id, 'name': name, 'cards': []}

        show_list_response = self.api.show_list(list_id)
        self.assertEqual(show_list, show_list_response)

    def test_add_card(self):
        name = 'test list'
        list_id = self.api.create_list(name, self.board_id)
        card_id = self.api.create_card('Test card', 'test des', list_id)
        self.assertIsInstance(list_id, str)

        show_list = {
            'id': list_id, 'name': name, 'cards': [
                {'id': card_id, 'name': 'Test card', 'description': 'test des', 'user': None}
            ]
        }

        show_list_response = self.api.show_list(list_id)
        self.assertEqual(show_list, show_list_response)

    def test_delete_list(self):
        name = 'test list'
        list_id = self.api.create_list(name, self.board_id)
        self.assertIsInstance(list_id, str)

        show_list = {'id': list_id, 'name': name, 'cards': []}

        show_list_response = self.api.show_list(list_id)
        self.assertEqual(show_list, show_list_response)

        self.api.delete_list(list_id)
        show_list = {}
        show_list_response = self.api.show_list(list_id)
        self.assertEqual(show_list, show_list_response)
