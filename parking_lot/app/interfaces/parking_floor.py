from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.interfaces.parking_spot import ParkingSpot
    from app.interfaces.parking_lot import ParkingLot


class ParkingFloor(ABC):
    @property
    @abstractmethod
    def id(self) -> int: pass

    @property
    @abstractmethod
    def spots(self) -> List[ParkingSpot]: pass

    @property
    @abstractmethod
    def parking_lot(self) -> ParkingLot: pass

    @abstractmethod
    def add_spot(self, spot: ParkingSpot) -> None: pass

    @abstractmethod
    def remove_spot(self, spot: ParkingSpot) -> None: pass

