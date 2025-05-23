import sys
import json

def fill(node, lookup):
    if isinstance(node, dict):
        node_id = node.get("id")
        if node_id in lookup and "value" in node:
            node["value"] = lookup[node_id]
        for child in node.values():
            fill(child, lookup)
    elif isinstance(node, list):
        for item in node:
            fill(item, lookup)

def main():
    if len(sys.argv) != 4:
        print("Использование: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_file, tests_file, report_file = sys.argv[1:]

    with open(values_file, encoding="utf-8") as vf:
        values_data = json.load(vf)
    lookup = {item["id"]: item["value"] for item in values_data.get("values", [])}

    with open(tests_file, encoding="utf-8") as tf:
        tests_data = json.load(tf)
    fill(tests_data, lookup)

    with open(report_file, "w", encoding="utf-8") as rf:
        json.dump(tests_data, rf, ensure_ascii=False, indent=2)

main()
