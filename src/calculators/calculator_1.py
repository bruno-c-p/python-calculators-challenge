from typing import Dict
from flask import Request
from src.errors.http_unprocesable_entity import HttpUnprocessableEntityError

class Calculator1:
    def calculate(self, request: Request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        number_divided_by_three = input_data / 3
        first_result = self.__first_process(number_divided_by_three)
        second_result = self.__second_process(number_divided_by_three)
        calculated_result = first_result + second_result + number_divided_by_three
        response = self.__format_response(calculated_result)
        return response

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("number is required")
        input_data = body["number"]
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part

    def __second_process(self, second_number: float) -> float:
        first_part = (second_number ** 2.121)
        second_part = (first_part / 5) + 1
        return second_part
    
    def __format_response(self, result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(result, 2)
            }
        }