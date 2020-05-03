from abc import ABC, abstractmethod


# TODO: Add a factory to build LB


class ServerInterface(ABC):
    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def max_request_limit(self) -> int: pass

    @property
    @abstractmethod
    def current_requests(self) -> int: pass

    @abstractmethod
    def serve(self, request_id: str) -> bool: pass

    @abstractmethod
    def clean_severed_requests(self) -> None: pass

    @property
    @abstractmethod
    def factor(self) -> float: pass

    @factor.setter
    @abstractmethod
    def factor(self, value) -> float: pass
