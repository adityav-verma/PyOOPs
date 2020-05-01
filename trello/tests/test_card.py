import unittest

from app.constants import BoardPrivacy
from app.trello import Trello
from app.models.user import User


class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.api = Trello()
        self.board_id = self.api.create_board('test board', BoardPrivacy.PUBLIC)
        self.list_id = self.api.create_list('test list', self.board_id)

    def test_create_card(self):
        name = 'card'
        description = 'desc'
        card_id = self.api.create_card(name, description, self.list_id)

        self.assertIsInstance(card_id, str)

        show_card = {
            'id': card_id, 'name': name, 'description': description, 'user': None
        }

        show_card_response = self.api.show_card(card_id)

        self.assertEqual(show_card, show_card_response)

    def test_assign_card(self):
        name = 'card'
        description = 'desc'
        card_id = self.api.create_card(name, description, self.list_id)
        user = User()

        self.api.assign_user_to_card(card_id, user)

        show_card = {
            'id': card_id, 'name': name, 'description': description, 'user': user
        }

        show_card_response = self.api.show_card(card_id)

        self.assertEqual(show_card, show_card_response)

    def test_unassign_card(self):
        name = 'card'
        description = 'desc'
        card_id = self.api.create_card(name, description, self.list_id)
        user = User()

        self.api.assign_user_to_card(card_id, user)
        show_card = {
            'id': card_id, 'name': name, 'description': description, 'user': user
        }
        show_card_response = self.api.show_card(card_id)
        self.assertEqual(show_card, show_card_response)

        self.api.un_assign_user_from_card(card_id, user)
        show_card = {
            'id': card_id, 'name': name, 'description': description, 'user': None
        }
        show_card_response = self.api.show_card(card_id)
        self.assertEqual(show_card, show_card_response)

    def test_show_card(self):
        name = 'card'
        description = 'desc'
        card_id = self.api.create_card(name, description, self.list_id)
        user = User()

        self.api.assign_user_to_card(card_id, user)

        show_card = {
            'id': card_id, 'name': name, 'description': description, 'user': user
        }

        show_card_response = self.api.show_card(card_id)

    def test_delete_card(self):
        name = 'card'
        description = 'desc'
        card_id = self.api.create_card(name, description, self.list_id)
        user = User()

        self.api.assign_user_to_card(card_id, user)

        show_card = {
            'id': card_id, 'name': name, 'description': description, 'user': user
        }

        show_card_response = self.api.show_card(card_id)

        self.api.delete_card(card_id)
        show_card = {}
        show_card_response = self.api.show_card(card_id)
        self.assertEqual(show_card, show_card_response)
