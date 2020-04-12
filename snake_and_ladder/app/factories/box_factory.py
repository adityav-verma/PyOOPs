from app.box import Box, Snake, Ladder
from app.interfaces.box_interface import BoxInterface
from app.interfaces.factories.box_factory_interface import BoxFactoryInterface


class BoxFactory(BoxFactoryInterface):

    @staticmethod
    def create_ladder(position, next_position) -> BoxInterface:
        return Ladder(position, next_position)

    @staticmethod
    def create_snake(position, next_position) -> BoxInterface:
        return Snake(position, next_position)

    @staticmethod
    def create_box(position) -> BoxInterface:
        return Box(position)