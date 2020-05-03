from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

from app.interfaces.payment import Payment

if TYPE_CHECKING:
    from app.interfaces.vehicle import Vehicle
    from app.interfaces.parking_spot import ParkingSpot


class Ticket(ABC):
    @property
    @abstractmethod
    def id(self): pass

    @property
    @abstractmethod
    def vehicle(self) -> Vehicle: pass

    @vehicle.setter
    @abstractmethod
    def vehicle(self, value: Vehicle) -> None: pass

    @property
    @abstractmethod
    def payment(self) -> Payment: pass

    @payment.setter
    @abstractmethod
    def payment(self, value: Payment) -> None: pass

    @property
    @abstractmethod
    def parking_spot(self) -> ParkingSpot: pass

    @parking_spot.setter
    @abstractmethod
    def parking_spot(self, value: ParkingSpot) -> None: pass

    @property
    @abstractmethod
    def issued_at(self) -> datetime: pass

    @issued_at.setter
    @abstractmethod
    def issued_at(self, value: datetime): pass