from abc import ABC, abstractmethod

from app.constants import EntitySize
from app.interfaces.ticket import Ticket


class Vehicle(ABC):
    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def size(self) -> EntitySize: pass

    @property
    @abstractmethod
    def ticket(self) -> Ticket: pass

    @ticket.setter
    @abstractmethod
    def ticket(self, value: Ticket): pass
