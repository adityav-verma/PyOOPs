from abc import ABC, abstractmethod

from app.constants import EntitySize
from app.interfaces.parking_floor import ParkingFloor
from app.interfaces.parking_lot import ParkingLot
from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.parking_strategy import ParkingStrategy
from app.interfaces.payment_strategy import PaymentStrategy


class Factory(ABC):
    @abstractmethod
    def create_parking_lot(self, parking_strategy: ParkingStrategy, payment_strategy: PaymentStrategy) -> ParkingLot: pass

    @abstractmethod
    def create_parking_floor(self, id: int, parking_lot: ParkingLot) -> ParkingFloor: pass

    @abstractmethod
    def create_parking_spot(self, id: int, size: EntitySize, parking_floor: ParkingFloor) -> ParkingSpot: pass

    @abstractmethod
    def create_parking_strategy(self) -> ParkingStrategy: pass

    @abstractmethod
    def create_payment_strategy(self) -> PaymentStrategy: pass

