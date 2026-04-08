import json
import jsonschema
import os

def test_schema_validity():
    with open("schema.json", "r") as f:
        schema = json.load(f)

    # Example data to test against
    data = {"indicator": "GDP", "value": 2.6, "year": 2025}
    jsonschema.validate(instance=data, schema=schema)

def test_schema_file_exists():
    assert os.path.exists("schema.json")
