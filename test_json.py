import json

from jsonschema import validate


def test_orgs():
    with open('orgs.schema.json') as schema_file:
        schema = json.load(schema_file)

    with open('orgs.json') as data_file:
        data = json.load(data_file)

    validate(data, schema)
