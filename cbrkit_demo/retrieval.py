import cbrkit
import cbrkit.sim

from cbrkit_demo.model import SnowDecisionFrame

casebase: dict[int, SnowDecisionFrame] = cbrkit.loaders.json("data/snow_cases_normalized.json")
query: SnowDecisionFrame = {
    "season": "early winter",
    "snow_type": "Ceavvi",
    "description": "Thin ice crust on top of snowpack",
    "physical_properties": {
        "ice": "Ice on the ground encapsulating plants",
        "crust": "Thin crust on top of snow pack",
        "packed_snow": "Slightly packed snow",
        "wet_snow": 0,
        "other_properties": "Some granular snow beneath the crust"
    },
    "scientific_reading": {
        "density_g_dm3": "medium",
        "hardness": "medium-high"
    },
    "herding_relevance": {
        "digestion_issues": 0,
        "mould_growth": 0,
        "harmful_conditions": 0,
        "food_accessibility": 70,
        "splittrad_hjord": 0,
        "grazing_conditions": "favorable",
        "reindeer_capacity": "high"
    }
}

# --- Similarity model ---
global_similarity = cbrkit.sim.attribute_value(
    attributes={
        # Contextual / categorical features
        "season": cbrkit.sim.strings.levenshtein(case_sensitive=False),
        "snow_type": cbrkit.sim.strings.levenshtein(case_sensitive=False),
        "description": cbrkit.sim.strings.levenshtein(case_sensitive=False),

        # Physical properties
        "physical_properties": cbrkit.sim.attribute_value(
            attributes={
                "ice": cbrkit.sim.strings.levenshtein(),
                "crust": cbrkit.sim.strings.levenshtein(),
                "packed_snow": cbrkit.sim.strings.levenshtein(),
                "wet_snow": cbrkit.sim.numbers.linear(50),
                "other_properties": cbrkit.sim.strings.levenshtein(),
            },
            aggregator=cbrkit.sim.aggregator(pooling="mean"),
        ),

        # Scientific reading
        "scientific_reading": cbrkit.sim.attribute_value(
            attributes={
                "type": cbrkit.sim.strings.levenshtein(),
                "density_g_dm3": cbrkit.sim.strings.levenshtein(),
                "hardness": cbrkit.sim.strings.levenshtein(),
            },
            aggregator=cbrkit.sim.aggregator(pooling="mean"),
        ),

        # Herding relevance
        "herding_relevance": cbrkit.sim.attribute_value(
            attributes={
                "digestion_issues": cbrkit.sim.numbers.linear(50),
                "mould_growth": cbrkit.sim.numbers.linear(50),
                "harmful_conditions": cbrkit.sim.numbers.linear(50),
                "food_accessibility": cbrkit.sim.numbers.linear(50),
                "splittrad_hjord": cbrkit.sim.numbers.linear(50),
                "grazing_conditions": cbrkit.sim.strings.levenshtein(),
                "reindeer_capacity": cbrkit.sim.strings.levenshtein(),
            },
            aggregator=cbrkit.sim.aggregator(pooling="mean"),
        ),
    },
    # weights={
    #     "season": 0.1,
    #     "snow_type": 0.2,
    #     "description": 0.1,
    #     "physical_properties": 0.25,
    #     "scientific_reading": 0.2,
    #     "herding_relevance": 0.15,
    # },
    aggregator=cbrkit.sim.aggregator(pooling="mean"),
)

def run_default():
    retriever = cbrkit.retrieval.build(global_similarity, limit=5)
    return cbrkit.retrieval.apply(casebase, query, retriever)

def run_macfac():
    pass
