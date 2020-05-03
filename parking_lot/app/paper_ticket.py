import uuid
from datetime import datetime
from typing import Optional

from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.payment import Payment
from app.interfaces.ticket import Ticket
from app.interfaces.vehicle import Vehicle


class PaperTicket(Ticket):

    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self._id = str(uuid.uuid4())
        self._vehicle = vehicle
        self._spot = spot

        self._payment: Optional[Payment] = None
        self._issued_at: datetime = datetime.utcnow()

    @property
    def id(self):
        return self._id

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle

    @property
    def parking_spot(self) -> ParkingSpot:
        return self._spot

    @property
    def payment(self) -> Payment:
        return self._payment

    @payment.setter
    def payment(self, value: Payment):
        self._payment = value

    @property
    def issued_at(self) -> datetime:
        return self._issued_at

    @issued_at.setter
    def issued_at(self, value: datetime):
        self._issued_at = value
