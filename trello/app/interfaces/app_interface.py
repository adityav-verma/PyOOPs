from abc import ABC, abstractmethod


class AppInterface(ABC):

    @abstractmethod
    def create_board(self, name: str, privacy: str) -> str:
        pass

    @abstractmethod
    def create_list(self, name: str, board_id: str) -> str:
        pass

    @abstractmethod
    def create_card(self, name: str, description: str, list_id: str) -> str:
        pass

    @abstractmethod
    def create_user(self, name: str, email: str) -> str:
        pass

    @abstractmethod
    def add_user_to_board(self, board_id: str, user_id: str):
        pass

    @abstractmethod
    def add_user_to_card(self, card_id: str, user_id: str):
        pass

    @abstractmethod
    def show_board(self, board_id: str):
        pass

    @abstractmethod
    def show_list(self, list_id: str):
        pass

    @abstractmethod
    def show_card(self, card_id: str):
        pass
