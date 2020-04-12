from abc import abstractmethod, ABC

from app.interfaces.box_interface import BoxInterface


class BoxFactoryInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_box(position) -> BoxInterface: pass

    @staticmethod
    @abstractmethod
    def create_snake(position, next_position) -> BoxInterface: pass

    @staticmethod
    @abstractmethod
    def create_ladder(position, next_position) -> BoxInterface: pass
