from flask import Flask, request, jsonify
from src.api.utils import validate_request
from src.api.validators import validate_dosage, validate_patient, validate_drug
from src.core.calculation_engine import CalculationEngine
from src.safety.validation_engine import SafetyValidationEngine

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
@validate_request(validate_patient, validate_drug)
def calculate_dosage():
    patient = request.json['patient']
    drug = request.json['drug']

    try:
        dosage = CalculationEngine.calculate_dosage(patient=patient, drug=drug)
        safe = SafetyValidationEngine.check_interactions(patient=patient, drug=drug)
        response = {
            'dosage': dosage,
            'safe': safe,
        }
    except Exception as e:
        response = {'error': str(e)}

    return jsonify(response), 200