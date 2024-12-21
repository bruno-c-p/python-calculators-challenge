from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3
    
class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 10000000
    
def test_calculate():
    mock_request = MockRequest(body={"numbers": [1, 1, 1, 1, 100]})
    driver = MockDriverHandler()
    calculator = Calculator3(driver)
    response = calculator.calculate(mock_request)
    assert isinstance(response, dict)
    assert response == {
        "data": {
            "Calculator": 3,
            "result": 10000000,
            "Success": True
        }
    }

def test_calculate_with_variance_error():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    driver = MockDriverHandlerError()
    calculator = Calculator3(driver)
    with raises(Exception) as exception_info:
        calculator.calculate(mock_request)
    assert str(exception_info.value) == "('Variance is less than multiplication', 400)"

def test_calculate_with_invalid_body():
    mock_request = MockRequest(body={})
    driver = MockDriverHandler()
    calculator = Calculator3(driver)
    with raises(Exception) as exception_info:
        calculator.calculate(mock_request)
    assert str(exception_info.value) == "('numbers is required', 422)"