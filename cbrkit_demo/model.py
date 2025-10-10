# Simple decision scenario representation.
from typing import TypedDict

class DecisionFrame(TypedDict, total=False):
    context: str
    activity: str
    temperature: int
    water_clarity: str

class SnowDecisionFrame(TypedDict, total=False):
    """Represents a snow-related TEK case with scientific links."""
    context: str  # e.g., "early winter"
    snow_type: str  # e.g., "bihci"
    translation: str  # e.g., "thin icy frost on vegetation"
    physical_properties: str  # "density_g_dm3; >500;hardness; very high"
    scientific_reading: str  # "hazard; ice formation; effect; blocks vegetation"
    effect_on_reindeer: str  # short narrative outcome
