from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
        
def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator = Calculator1()
    response = calculator.calculate(mock_request)
    assert 'data' in response
    assert 'Calculator' in response['data']
    assert 'result' in response['data']
    assert response['data']['result'] == 14.25
    assert response['data']['Calculator'] == 1

def test_calculate_with_invalid_body():
    mock_request = MockRequest(body={})
    calculator = Calculator1()
    with raises(Exception) as exception_info:
        calculator.calculate(mock_request)
    assert str(exception_info.value) == "('number is required', 422)"