# Simple decision scenario representation.
from typing import TypedDict

class SnowDecisionFrame(TypedDict, total=False):
    """Represents a snow-related TEK case with scientific links."""
    season: str  # e.g., "early winter"
    snow_type: str  # e.g., "bihci"
    description: str  # e.g., "thin icy frost on vegetation"
    physical_properties: dict  # {"density_g_dm3": ">500", "hardness": "very high"}
    scientific_reading: dict  # {"hazard": "ice formation", "effect": "blocks vegetation"}
    herding_relevance: dict  # {"narrative": "This snow type is crucial for reindeer grazing."}
