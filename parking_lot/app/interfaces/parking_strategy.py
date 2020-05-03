from abc import ABC, abstractmethod

from app.interfaces.parking_lot import ParkingLot
from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.vehicle import Vehicle


class ParkingStrategy(ABC):
    @abstractmethod
    def find_spot(self, parking_lot: ParkingLot, vehicle: Vehicle) -> ParkingSpot: pass
