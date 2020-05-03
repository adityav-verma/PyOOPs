from app.constants import EntitySize
from app.generic_parking_floor import GenericParkingFloor
from app.generic_parking_lot import GenericParkingLot
from app.generic_parking_spot import GenericParkingSpot
from app.generic_parking_strategy import GenericParkingStrategy
from app.generic_payment_strategy import GenericPaymentStrategy
from app.interfaces.factory import Factory
from app.interfaces.parking_floor import ParkingFloor
from app.interfaces.parking_lot import ParkingLot
from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.parking_strategy import ParkingStrategy
from app.interfaces.payment_strategy import PaymentStrategy


class GenericFactory(Factory):
    def create_parking_lot(self, parking_strategy: ParkingStrategy, payment_strategy: PaymentStrategy) -> ParkingLot:
        return GenericParkingLot(parking_strategy, payment_strategy)

    def create_parking_floor(self, id: int, parking_lot: ParkingLot) -> ParkingFloor:
        return GenericParkingFloor(id, parking_lot)

    def create_parking_spot(self, id: int, size: EntitySize, parking_floor: ParkingFloor) -> ParkingSpot:
        return GenericParkingSpot(id, size, parking_floor)

    def create_parking_strategy(self) -> ParkingStrategy:
        return GenericParkingStrategy()

    def create_payment_strategy(self) -> PaymentStrategy:
        return GenericPaymentStrategy()
