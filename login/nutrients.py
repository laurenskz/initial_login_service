from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Objective:
    nutrient1: str
    min: float
    max: Optional[float] = None


@dataclass
class VitaminsAndMinerals:
    name: str
    description: str
    objectives: List[Objective]


NUTRIENT_DATA = VitaminsAndMinerals(
    name="Vitamins and minerals",
    description="The Recommended Dietary Intake (RDI) of vitamins represents the daily nutrient levels that are considered sufficient to meet the needs of most healthy individuals. These guidelines are established to ensure that people receive essential vitamins to maintain good health and prevent deficiencies.",
    objectives=[
        Objective(nutrient1="vitamin_a", min=3000, max=10000),
        Objective(nutrient1="vitamin_b1", min=1.2),
        Objective(nutrient1="vitamin_b2", min=1.3),
        Objective(nutrient1="vitamin_b3", min=16, max=35),
        Objective(nutrient1="vitamin_b5", min=5),
        Objective(nutrient1="vitamin_b6", min=1.7, max=100),
        Objective(nutrient1="vitamin_b9", min=200, max=1000),
        Objective(nutrient1="vitamin_b12", min=2.4),
        Objective(nutrient1="vitamin_c", min=90, max=2000),
        Objective(nutrient1="vitamin_d", min=15, max=100),
        Objective(nutrient1="vitamin_e", min=15, max=1000),
        Objective(nutrient1="vitamin_k", min=120, max=9999),
        Objective(nutrient1="calcium", min=1000, max=2500),
        Objective(nutrient1="copper", min=900, max=10000),
        Objective(nutrient1="iron", min=18, max=45),
        Objective(nutrient1="magnesium", min=420, max=1000),
        Objective(nutrient1="manganese", min=2.3, max=11),
        Objective(nutrient1="phosphorus", min=1250, max=4000),
        Objective(nutrient1="selenium", min=55, max=400),
        Objective(nutrient1="zinc", min=11, max=40),
        Objective(nutrient1="potassium", min=4700, max=9500),
        Objective(nutrient1="sodium", min=0, max=2300)
    ]
)
