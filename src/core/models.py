from dataclasses import dataclass
from typing import Optional

@dataclass
class Patient:
    name: str
    weight_kg: float
    age: int
    condition: str
    weight_status: Optional[str] = None

@dataclass
class Drug:
    name: str
    dose_per_kg: float
    dose_unit: str
    half_life: float
    route_of_administration: str
