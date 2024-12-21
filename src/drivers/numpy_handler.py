from typing import List
import numpy
from .interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__numpy = numpy

    def standard_deviation(self, numbers: List[float]) -> float:
        return self.__numpy.std(numbers)
    
    def variance(self, numbers: List[float]) -> float:
        return self.__numpy.var(numbers)