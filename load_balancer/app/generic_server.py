import time
import uuid
from collections import deque
from typing import Deque, List

from app.interfaces.server_interface import ServerInterface


class GenericServer(ServerInterface):
    def __init__(self, max_request_limit: int, factor: int, id: str = None):
        self._id = str(uuid.uuid4()) if not id else id
        self._max_request_limit = max_request_limit
        self._factor = factor
        self._current_requests: Deque[List[str, float]] = deque()

        self._last_updated_at = None

    @property
    def current_requests(self) -> int:
        return len(self._current_requests)

    def serve(self, request_id: str) -> bool:
        if len(self._current_requests) >= self.max_request_limit:
            return False

        self._current_requests.append([request_id, time.time()])
        self._last_updated_at = time.time()

        return True

    def clean_severed_requests(self) -> None:
        curr_time = time.time()
        if not self.current_requests:
            return

        while self.current_requests:
            top = self._current_requests[0]
            if top[1] + 0.0001 < curr_time:
                self._current_requests.popleft()
            else:
                return

    @property
    def id(self) -> str:
        return self._id

    @property
    def max_request_limit(self) -> int:
        return self._max_request_limit

    @property
    def factor(self) -> float:
        return self._factor

    @factor.setter
    def factor(self, value):
        self._factor = value
