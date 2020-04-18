import uuid

from app.interfaces.card_interface import CardInterface
from app.interfaces.user_interface import UserInterface


class Card(CardInterface):
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._id = str(uuid.uuid4())
        self._user: UserInterface or None = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def user(self) -> UserInterface:
        return self._user

    def add_user(self, user: UserInterface):
        self._user = user

