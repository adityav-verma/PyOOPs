from abc import ABC, abstractmethod

from app.interfaces.ticket import Ticket


class PaymentStrategy(ABC):
    @abstractmethod
    def get_charge(self, ticket: Ticket) -> int: pass