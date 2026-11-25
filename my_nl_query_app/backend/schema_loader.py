import json
import yaml

def load_schema(file_path):
    with open(file_path, "r") as f:
        if file_path.endswith(".json"):
            return json.load(f)
        elif file_path.endswith(".yaml"):
            return yaml.safe_load(f)
    return None