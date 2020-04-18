from abc import ABC, abstractmethod

from app.interfaces.user_interface import UserInterface


class CardInterface(ABC):
    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def user(self) -> UserInterface: pass

    @user.setter
    @abstractmethod
    def user(self, user: UserInterface):
        pass
