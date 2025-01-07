from abc import ABC, abstractmethod
import time


class RateLimitService(ABC):
    """"""

    _max_request_per_window: int
    _seconds_per_window: int

    def __init__(self, max_request_per_window: int, seconds_per_window: int):
        self._max_request_per_window = max_request_per_window
        self._seconds_per_window = seconds_per_window