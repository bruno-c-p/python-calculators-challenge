from typing import List
from abc import ABC, abstractmethod

class DriverHandlerInterface(ABC):
    @abstractmethod
    def standard_deviation(self, numbers: List[float]) -> float:
        pass

    @abstractmethod
    def variance(self, numbers: List[float]) -> float:
        pass