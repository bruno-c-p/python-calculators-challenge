from flask import Blueprint, request, jsonify
from src.calculators.calculator_1 import Calculator1
from src.main.factories.calculator_2_factory import calculator_2_factory
from src.main.factories.calculator_3_factory import calculator_3_factory
from src.calculators.calculator_4 import Calculator4
from src.errors.error_controller import handle_errors

calculators_routes_bp = Blueprint('calculators_routes', __name__)

@calculators_routes_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calculator = Calculator1()
    try:
        response = calculator.calculate(request)
        return jsonify(response), 200
    except Exception as error:
        response, status = handle_errors(error)
        return jsonify(response), status

@calculators_routes_bp.route('/calculator/2', methods=['POST'])
def calculator_2():
    calculator = calculator_2_factory()
    try:
        response = calculator.calculate(request)
        return jsonify(response), 200
    except Exception as error:
        response, status = handle_errors(error)
        return jsonify(response), status

@calculators_routes_bp.route('/calculator/3', methods=['POST'])
def calculator_3():
    calculator = calculator_3_factory()
    try:
        response = calculator.calculate(request)
        return jsonify(response), 200
    except Exception as error:
        response, status = handle_errors(error)
        return jsonify(response), status
    
@calculators_routes_bp.route('/calculator/4', methods=['POST'])
def calculator_4():
    calculator = Calculator4()
    try:
        response = calculator.calculate(request)
        return jsonify(response), 200
    except Exception as error:
        response, status = handle_errors(error)
        return jsonify(response), status