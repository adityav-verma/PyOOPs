from abc import ABC, abstractmethod

from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.ticket import Ticket
from app.interfaces.vehicle import Vehicle


class ParkingCommand(ABC):
    @abstractmethod
    def execute(self) -> Ticket: pass

    @property
    @abstractmethod
    def vehicle(self) -> Vehicle: pass

    @property
    @abstractmethod
    def parking_spot(self) -> ParkingSpot: pass
