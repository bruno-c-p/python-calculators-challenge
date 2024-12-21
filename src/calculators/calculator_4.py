from typing import Dict, List
from flask import Request
from src.errors.http_unprocesable_entity import HttpUnprocessableEntityError

class Calculator4:
    def calculate(self, request: Request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        mean = self.__calculate_mean(input_data)
        response = self.__format_response(mean)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("numbers is required")
        input_data = body["numbers"]
        return input_data
    
    def __calculate_mean(self, numbers: List[float]) -> float:
        sum = 0
        for num in numbers: sum += num
        return sum / len(numbers)
    
    def __format_response(self, result: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": result
            }
        }