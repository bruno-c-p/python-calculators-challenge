from typing import Dict, List
from pytest import raises
from .calculator_2 import Calculator2

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3
        
def test_calculate():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver = MockDriverHandler()
    calculator = Calculator2(driver)
    response = calculator.calculate(mock_request)
    assert isinstance(response, dict)
    assert response == {
        "data": {
            "Calculator": 2,
            "result": 0.33
        }
    }

def test_calculate_with_invalid_body():
    mock_request = MockRequest(body={})
    driver = MockDriverHandler()
    calculator = Calculator2(driver)
    with raises(Exception) as exception_info:
        calculator.calculate(mock_request)
    assert str(exception_info.value) == "('numbers is required', 422)"