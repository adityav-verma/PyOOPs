from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

from app.interfaces.models.card_interface import CardInterface
from app.interfaces.models.component_interface import Component

if TYPE_CHECKING:
    from app.interfaces.models.board_interface import BoardInterface


class BoardListInterface(Component, ABC):
    pass
