from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING, Optional

from app.interfaces.payment import Payment
from app.interfaces.ticket import Ticket
from app.interfaces.vehicle import Vehicle

if TYPE_CHECKING:
    from app.interfaces.parking_floor import ParkingFloor


class ParkingLot(ABC):
    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def floors(self) -> List[ParkingFloor]: pass

    @abstractmethod
    def add_floor(self, floor: ParkingFloor) -> None: pass

    @abstractmethod
    def remove_floor(self, floor: ParkingFloor) -> None: pass

    @abstractmethod
    def park(self, vehicle: Vehicle) -> Optional[Ticket]: pass

    @abstractmethod
    def checkout(self, ticket: Ticket) -> Payment: pass
