from src.safety.models import DrugInteraction, Patient
from src.utils.errors import InvalidInputError

class SafetyValidationEngine:
    @staticmethod
    def check_interactions(patient: Patient, drug: Drug) -> bool:
        """
        Checks for drug interactions based on patient conditions and drug properties.

        Args:
            patient (Patient): Patient object containing conditions and other relevant information.
            drug (Drug): Drug object containing the drug properties.

        Returns:
            bool: True if interactions are safe, False otherwise.

        Raises:
            InvalidInputError: If patient or drug information is invalid.
        """
        if not patient or not drug:
            raise InvalidInputError("Patient and drug information must be provided.")

        # Check for known interactions
        for interaction in DrugInteraction:
            if interaction.condition in patient.condition and interaction.drug == drug.name:
                return False

        return True