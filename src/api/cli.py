import click
from src.api.utils import validate_request
from src.api.validators import validate_dosage, validate_patient, validate_drug
from src.core.calculation_engine import CalculationEngine
from src.safety.validation_engine import SafetyValidationEngine

@click.command()
@click.option('--patient', required=True, type=dict, help='Patient information')
@click.option('--drug', required=True, type=dict, help='Drug information')
def calculate_dosage_cli(patient, drug):
    try:
        patient = validate_patient(patient)
        drug = validate_drug(drug)
        dosage = CalculationEngine.calculate_dosage(patient=patient, drug=drug)
        safe = SafetyValidationEngine.check_interactions(patient=patient, drug=drug)
        click.echo(f'Dosage: {dosage} {drug[