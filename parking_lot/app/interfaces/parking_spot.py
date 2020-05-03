from abc import ABC, abstractmethod

from app.constants import EntitySize
from app.interfaces.parking_floor import ParkingFloor
from app.interfaces.vehicle import Vehicle


class ParkingSpot(ABC):
    @property
    @abstractmethod
    def id(self) -> int: pass

    @property
    @abstractmethod
    def size(self) -> EntitySize: pass

    @property
    @abstractmethod
    def floor(self) -> ParkingFloor: pass

    @property
    @abstractmethod
    def vehicle(self) -> Vehicle: pass

    @vehicle.setter
    @abstractmethod
    def vehicle(self, value: Vehicle): pass
