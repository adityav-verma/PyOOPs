from typing import Optional

from app.constants import EntitySize
from app.interfaces.ticket import Ticket
from app.interfaces.vehicle import Vehicle


class GenericVehicle(Vehicle):
    def __init__(self, id: str, size: EntitySize):
        self._size = size
        self._id = id
        self._ticket: Optional[Ticket ]= None

    @property
    def id(self) -> str:
        return self._id

    @property
    def size(self) -> EntitySize:
        return self._size

    @property
    def ticket(self) -> Ticket:
        return self._ticket

    @ticket.setter
    def ticket(self, value: Ticket):
        self._ticket = value


class MotorBike(GenericVehicle):
    def __init__(self, id: str):
        super(MotorBike, self).__init__(id, EntitySize.SMALL)


class Car(GenericVehicle):
    def __init__(self, id: str):
        super(Car, self).__init__(id, EntitySize.MEDIUM)


class LargeCar(GenericVehicle):
    def __init__(self, id: str):
        super(LargeCar, self).__init__(id, EntitySize.LARGE)


class XLargeCard(GenericVehicle):
    def __init__(self, id: str):
        super(XLargeCard, self).__init__(id, EntitySize.XLARGE)
