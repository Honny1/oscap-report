import json

from jsonschema import validate


def main():
    json_schema = None
    json_data = None

    with open("../JSON/json_schema_of_report.json", "r", encoding="utf-8") as schema_file:
        json_schema = json.load(schema_file)

    with open("../JSON/example_report.json", "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)

    validate(json_data, json_schema)


if __name__ == "__main__":
    main()
