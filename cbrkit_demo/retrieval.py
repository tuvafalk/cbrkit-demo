import cbrkit

from cbrkit_demo.model import DecisionFrame, SnowDecisionFrame

casebase: dict[int, SnowDecisionFrame] = cbrkit.loaders.json("data/snow_cases.json")
query: SnowDecisionFrame = {
    "context": "early winter",
    "snow_type": "Ceavvi",  
    "translation": "hard-packed snow",
    "physical_properties": "hardness: medium-high",
    "scientific_reading": "hazard: reduced pasture access",
    "effect_on_reindeer": "moderate difficulty grazing"
}

# Update similarity model to handle only the relevant attributes
global_similarity = cbrkit.sim.attribute_value(
    attributes={
            "snow_type": cbrkit.sim.strings.taxonomy.load(
            "data/taxonomies/snow_type.yaml",
            measure=cbrkit.sim.strings.taxonomy.path_steps(),
        ),
        "context": cbrkit.sim.strings.levenshtein(case_sensitive=False),
    },
    aggregator=cbrkit.sim.aggregator("mean"),
)

def run_default():
    retriever = cbrkit.retrieval.build(global_similarity, limit=5)
    return cbrkit.retrieval.apply(casebase, query, retriever)

def run_macfac():
    pass
