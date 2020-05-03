from typing import Optional

from app.constants import EntitySize
from app.interfaces.parking_floor import ParkingFloor
from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.vehicle import Vehicle


class GenericParkingSpot(ParkingSpot):
    def __init__(self, id: int, size: EntitySize, floor: ParkingFloor):
        self._id = id
        self._size = size
        self._floor = floor

        self._vehicle: Optional[Vehicle] = None

    def __str__(self):
        return f'Id: {self._id}, Size: {self._size.value}, Floor: {self._floor.id}'

    @property
    def id(self) -> int:
        return self._id

    @property
    def size(self) -> EntitySize:
        return self._size

    @property
    def floor(self) -> ParkingFloor:
        return self._floor

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle

    @vehicle.setter
    def vehicle(self, value: Vehicle):
        self._vehicle = value
