from app.card import Card
from app.interfaces.board_list_interface import BoardListInterface
from app.interfaces.card_factory_interface import CardFactoryInterface
from app.interfaces.card_interface import CardInterface


class CardFactory(CardFactoryInterface):
    def get_with_id(self, id: str) -> BoardListInterface:
        pass

    def create_card(self, name: str, description: str) -> CardInterface:
        return Card(name, description)

