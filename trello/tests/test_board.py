import unittest

from app.constants import BoardPrivacy
from app.trello import Trello, User


class TestBoardAPIs(unittest.TestCase):

    def setUp(self) -> None:
        self.api = Trello()

    def test_create_board(self):
        name = 'Test Board'
        privacy = BoardPrivacy.PUBLIC
        response = self.api.create_board(name, privacy)
        self.assertIsInstance(response, str)
        show_board = {
            'id': response,
            'name': name,
            'privacy': privacy.value,
            'members': []
        }

        show_board_repsonse = self.api.show_board(response)
        self.assertEqual(show_board, show_board_repsonse)

    def test_board_update(self):
        name = 'Test Board'
        privacy = BoardPrivacy.PUBLIC
        board_id = self.api.create_board(name, privacy)

        new_name = 'Test Board new'
        new_privacy = BoardPrivacy.PRIVATE

        self.api.update_board(board_id, new_name, new_privacy)
        show_board = {
            'id': board_id,
            'name': new_name,
            'privacy': new_privacy.value,
            'members': [],
            'board_lists': []
        }

        show_board_repsonse = self.api.show_board(board_id)
        self.assertEqual(show_board, show_board_repsonse)

    def test_show_board(self):
        name = 'Test Board'
        privacy = BoardPrivacy.PUBLIC
        board_id = self.api.create_board(name, privacy)

        show_board = {
            'id': board_id,
            'name': name,
            'privacy': privacy.value,
            'members': [],
            'board_lists': []
        }

        show_board_repsonse = self.api.show_board(board_id)
        self.assertEqual(show_board, show_board_repsonse)

    def test_add_member(self):
        name = 'Test Board'
        privacy = BoardPrivacy.PRIVATE
        board_id = self.api.create_board(name, privacy)

        user = User()
        user2 = User()
        self.api.add_members_to_board(board_id, user)
        self.api.add_members_to_board(board_id, user2)

        show_board = {
            'id': board_id,
            'name': name,
            'privacy': privacy.value,
            'members': [user, user2],
            'board_lists': []
        }
        show_board_repsonse = self.api.show_board(board_id)
        self.assertEqual(show_board, show_board_repsonse)

    def test_remove_member(self):
        name = 'Test Board'
        privacy = BoardPrivacy.PRIVATE
        board_id = self.api.create_board(name, privacy)

        user = User()
        user2 = User()
        self.api.add_members_to_board(board_id, user)
        self.api.add_members_to_board(board_id, user2)
        self.api.remove_members_from_board(board_id, user)

        show_board = {
            'id': board_id,
            'name': name,
            'privacy': privacy.value,
            'members': [user2],
            'board_lists': []
        }
        show_board_repsonse = self.api.show_board(board_id)
        self.assertEqual(show_board, show_board_repsonse)

    def test_delete_board(self):
        name = 'Test Board'
        privacy = BoardPrivacy.PRIVATE
        board_id = self.api.create_board(name, privacy)
        self.api.delete_board(board_id)

        show_board = {}
        show_board_repsonse = self.api.show_board(board_id)
        self.assertEqual(show_board, show_board_repsonse)

    def test_add_list_to_board(self):
        name = 'Test Board'
        privacy = BoardPrivacy.PRIVATE
        board_id = self.api.create_board(name, privacy)
        list_id = self.api.create_list('test list', board_id)
        show_board = {
            'id': board_id,
            'name': name,
            'privacy': privacy.value,
            'members': [],
            'board_lists': [list_id]
        }
        show_board_repsonse = self.api.show_board(board_id)
        self.assertEqual(show_board, show_board_repsonse)