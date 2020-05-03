from datetime import datetime
from math import ceil

from app.interfaces.payment_strategy import PaymentStrategy
from app.interfaces.ticket import Ticket


class GenericPaymentStrategy(PaymentStrategy):
    def __init__(self):
        self._hourly_charge = 2

    def get_charge(self, ticket: Ticket) -> int:
        curr_time = datetime.utcnow()
        diff = curr_time - ticket.issued_at
        hour = ceil(diff.seconds // 60)
        return hour * self._hourly_charge
