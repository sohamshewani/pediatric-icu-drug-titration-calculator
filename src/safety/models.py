from enum import Enum
from dataclasses import dataclass
from typing import Optional

@dataclass
class DrugInteraction:
    condition: str
    drug: str
    description: str

# Example interactions
class Condition(Enum):
    SEIZURES = "seizures"
    HEART_DISEASE = "heart disease"
    KIDNEY_FAILURE = "kidney failure"

class Drug(Enum):
    AMIODARONE = "amiodarone"
    CARBAZOLE = "carbazole"

interactions = [
    DrugInteraction(condition=Condition.SEIZURES.value, drug=Drug.AMIODARONE.value, description="Increased risk of seizures"),
    DrugInteraction(condition=Condition.HEART_DISEASE.value, drug=Drug.AMIODARONE.value, description="May exacerbate heart conditions"),
    DrugInteraction(condition=Condition.KIDNEY_FAILURE.value, drug=Drug.AMIODARONE.value, description="Increased risk of toxicity"),
    DrugInteraction(condition=Condition.SEIZURES.value, drug=Drug.CARBAZOLE.value, description="Increased risk of seizures"),
    DrugInteraction(condition=Condition.HEART_DISEASE.value, drug=Drug.CARBAZOLE.value, description="May exacerbate heart conditions"),
    DrugInteraction(condition=Condition.KIDNEY_FAILURE.value, drug=Drug.CARBAZOLE.value, description="Increased risk of toxicity"),
]