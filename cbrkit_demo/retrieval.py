import cbrkit

from cbrkit_demo.model import Car

casebase: dict[int, Car] = cbrkit.loaders.json("data/casebase.json")
query: Car = {}


global_similarity = cbrkit.sim.attribute_value(
    attributes={
        "year": cbrkit.sim.numbers.linear(max=100),
        "paint_color": cbrkit.sim.strings.taxonomy.load(
            "data/taxonomies/paint_color.yaml",
            measure=cbrkit.sim.strings.taxonomy.user_weights("optimistic"),
        ),
        "manufacturer": cbrkit.sim.strings.taxonomy.load(
            "data/taxonomies/manufacturer.yaml",
            measure=cbrkit.sim.strings.taxonomy.path_steps(),
        ),
    },
    types={
        str: cbrkit.sim.strings.levenshtein(),
        int: cbrkit.sim.numbers.linear(max=9999999),
    },
    aggregator=cbrkit.sim.aggregator("mean"),
)


def run_default():
    retriever = cbrkit.retrieval.build(global_similarity, limit=10)

    return cbrkit.retrieval.apply(casebase, query, retriever)


def run_macfac():
    pass
