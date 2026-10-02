from src.core.models import Patient, Drug
from src.utils.errors import InvalidInputError

class CalculationEngine:
    @staticmethod
    def calculate_dosage(patient: Patient, drug: Drug) -> float:
        """
        Calculates the dosage based on patient weight and drug properties.

        Args:
            patient (Patient): Patient object containing weight and other relevant information.
            drug (Drug): Drug object containing the drug properties.

        Returns:
            float: Calculated dosage.

        Raises:
            InvalidInputError: If patient or drug information is invalid.
        """
        if not patient or not drug:
            raise InvalidInputError("Patient and drug information must be provided.")

        # Perform dosage calculation based on weight and drug properties
        # Example: dosage = patient.weight * drug.dose_per_kg
        dosage = patient.weight * drug.dose_per_kg

        return dosage