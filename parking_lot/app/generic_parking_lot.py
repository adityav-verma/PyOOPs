import uuid
from typing import List, Optional

from app.generic_checkout_command import GenericCheckoutComamnd
from app.generic_parking_command import GenericParkingCommand
from app.interfaces.checkout_command import CheckoutCommand
from app.interfaces.parking_command import ParkingCommand
from app.interfaces.parking_floor import ParkingFloor
from app.interfaces.parking_lot import ParkingLot
from app.interfaces.parking_strategy import ParkingStrategy
from app.interfaces.payment_strategy import PaymentStrategy
from app.interfaces.ticket import Ticket
from app.interfaces.vehicle import Vehicle


class GenericParkingLot(ParkingLot):

    def __init__(self, parking_strategy: ParkingStrategy, payment_strategy: PaymentStrategy):
        self._id = str(uuid.uuid4())
        self._floors: List[ParkingFloor] = []
        self._parking_strategy = parking_strategy
        self._payment_strategy = payment_strategy
        self._parking_commands: List[ParkingCommand] = []
        self._checkout_commands: List[CheckoutCommand] = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def floors(self) -> List[ParkingFloor]:
        return self._floors

    def add_floor(self, floor: ParkingFloor) -> None:
        self._floors.append(floor)

    def remove_floor(self, floor: ParkingFloor) -> None:
        self._floors.remove(floor)

    def park(self, vehicle: Vehicle) -> Optional[Ticket]:
        spot = self._parking_strategy.find_spot(self, vehicle)
        parking_command = GenericParkingCommand(vehicle, spot)
        ticket = parking_command.execute()
        self._parking_commands.append(parking_command)
        return ticket

    def checkout(self, ticket: Ticket):
        charge = self._payment_strategy.get_charge(ticket)
        checkout_command = GenericCheckoutComamnd(ticket, charge)
        payment = checkout_command.execute()
        self._checkout_commands.append(checkout_command)
        return payment

