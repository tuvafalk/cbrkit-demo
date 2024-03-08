from collections.abc import Callable

import cbrkit

from cbrkit_demo.model import Car
from cbrkit_demo.retrieval import casebase, query, run_default, run_macfac


def run_task(
    name: str,
    run_func: Callable[
        [],
        cbrkit.retrieval.Result[int, Car, cbrkit.sim.AttributeValueSim[float]] | None,
    ],
):
    result = run_func()
    print(f"Results for task '{name}':")

    if not result:
        print("Not yet implemented.")
        return

    if len(result.intermediates) > 1:
        for i, intermediate in enumerate(result.intermediates):
            print(f"Retriever {i + 1} returned {len(intermediate.ranking)} cases")

    for rank, (case_id, sim) in enumerate(result.similarities.items()):
        print(f"Rank {rank + 1}: Case {case_id + 1}")
        print(f"  Case: {casebase[case_id]}")
        print(f"  Global similarity: {sim.value:.3f}")
        print(f"  Local similarities: {sim.by_attribute}")


print(f"Query: {query}")
print()
run_task("Default", run_default)
print()
run_task("MAC/FAC", run_macfac)
print()
