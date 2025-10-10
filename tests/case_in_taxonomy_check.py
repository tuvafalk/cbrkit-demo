import json, yaml

with open("data/snow_cases.json") as f: cases = json.load(f)
with open("data/taxonomies/snow_type.yaml") as f: taxonomy = yaml.safe_load(f)

case_types = {c["snow_type"] for c in cases}
def collect_names(node): 
    names = [node["name"]] 
    for child in node.get("children", []): 
        names.extend(collect_names(child)) 
    return names
tax_names = set(collect_names(taxonomy))

print("Missing:", case_types - tax_names)
print("Extra:", tax_names - case_types)