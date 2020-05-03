from app.cash_payment import CashPayment
from app.interfaces.checkout_command import CheckoutCommand
from app.interfaces.payment import Payment
from app.interfaces.ticket import Ticket


class GenericCheckoutComamnd(CheckoutCommand):
    def __init__(self, ticket: Ticket, charge: int):
        self._ticket = ticket
        self._charge = charge

    @property
    def ticket(self):
        return self._ticket

    def execute(self) -> Payment:
        payment = CashPayment(self._charge)
        self.ticket.payment = payment
        self.ticket.parking_spot.vehicle = None
        return payment
