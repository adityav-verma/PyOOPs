from abc import abstractmethod, ABC

from app.interfaces.payment import Payment
from app.interfaces.ticket import Ticket


class CheckoutCommand(ABC):
    @property
    @abstractmethod
    def ticket(self):
        pass

    @abstractmethod
    def execute(self) -> Payment: pass
