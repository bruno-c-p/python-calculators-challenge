from flask import Flask, request, jsonify
from src.main.routes.calculators import calculators_routes_bp

app = Flask(__name__)

app.register_blueprint(calculators_routes_bp)