from abc import ABC, abstractmethod


class Payment(ABC):
    @property
    @abstractmethod
    def charge(self) -> int: pass