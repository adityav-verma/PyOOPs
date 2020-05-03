from typing import List

from app.interfaces.parking_floor import ParkingFloor
from app.interfaces.parking_lot import ParkingLot
from app.interfaces.parking_spot import ParkingSpot


class GenericParkingFloor(ParkingFloor):
    def __init__(self, id: int, parking_lot: ParkingLot):
        self._id = id
        self._parking_lot = parking_lot

        self._spots: List[ParkingSpot] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def spots(self) -> List[ParkingSpot]:
        return self._spots

    @property
    def parking_lot(self) -> ParkingLot:
        return self._parking_lot

    def add_spot(self, spot: ParkingSpot) -> None:
        self._spots.append(spot)

    def remove_spot(self, spot: ParkingSpot) -> None:
        self._spots.remove(spot)
