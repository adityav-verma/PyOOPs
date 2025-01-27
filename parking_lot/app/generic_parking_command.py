from typing import Optional

from app.interfaces.parking_command import ParkingCommand
from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.ticket import Ticket
from app.interfaces.vehicle import Vehicle
from app.paper_ticket import PaperTicket


class GenericParkingCommand(ParkingCommand):
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot):
        self._vehicle = vehicle
        self._parking_spot = parking_spot
        self._ticket: Optional[Ticket] = None

    def __str__(self):
        return f'Vehicle: {self._vehicle}, Spot: {self._parking_spot}, Ticket: {self._ticket}'

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle

    @property
    def parking_spot(self) -> ParkingSpot:
        return self._parking_spot

    def execute(self) -> Ticket:
        ticket = PaperTicket(self._vehicle, self._parking_spot)
        self._parking_spot.vehicle = self._vehicle
        self._vehicle.ticket = ticket
        self._ticket = ticket
        return ticket
