from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
    
def test_calculate():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calculator = Calculator4()
    response = calculator.calculate(mock_request)
    assert isinstance(response, dict)
    assert response == {
        "data": {
            "Calculator": 4,
            "result": 3
        }
    }

def test_calculate_with_invalid_body():
    mock_request = MockRequest(body={})
    calculator = Calculator4()
    with raises(Exception) as exception_info:
        calculator.calculate(mock_request)
    assert str(exception_info.value) == "('numbers is required', 422)"