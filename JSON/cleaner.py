import json


def remove_data_from_groups_one(group):
    del group["description"]
    del group["title"]
    if group["sub_groups"]:
        for i in group["sub_groups"]:
            remove_data_from_groups_one(i)


def remove_data_from_groups(groups):
    for group in groups:
        remove_data_from_groups_one(groups[group])


if __name__ == "__main__":
    data = None
    with open("example_report.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    del data["score"]
    del data["score_max"]
    for rule in data["rules"]:
        del data["rules"][rule]["title"]
        del data["rules"][rule]["multi_check"]
        del data["rules"][rule]["identifiers"]
        del data["rules"][rule]["references"]
        del data["rules"][rule]["description"]
        del data["rules"][rule]["rationale"]
        del data["rules"][rule]["platforms"]
        del data["rules"][rule]["remediations"]
        del data["rules"][rule]["oval_tree"]
        del data["rules"][rule]["cpe_tree"]
    remove_data_from_groups(data["groups"])
    with open('json_data.json', 'w') as outfile:
        json.dump(data, outfile, indent="\t")
