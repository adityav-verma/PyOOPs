from __future__ import  annotations

from abc import ABC, abstractmethod
from typing import List, Union


class Component(ABC):

    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def name(self) -> str: pass

    @name.setter
    @abstractmethod
    def name(self, value: str) -> None: pass

    @property
    @abstractmethod
    def parent(self) -> Union[Component, None]: pass

    @parent.setter
    @abstractmethod
    def parent(self, value) -> None: pass

    @property
    @abstractmethod
    def children(self) -> List[Component]: pass

    @abstractmethod
    def add_child_component(self, child: Component) -> None: pass

    @abstractmethod
    def remove_child_component(self, child: Component) -> None: pass
