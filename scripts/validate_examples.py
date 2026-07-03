import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Agent Handoff Record",
        "schema": ROOT / "schemas" / "agent-handoff-record.schema.json",
        "example": ROOT / "examples" / "agent-handoff-record.example.yaml",
    }
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_target(target):
    schema = load_json(target["schema"])
    example = load_yaml(target["example"])

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda e: e.path)

    print(f"[validate] {target['name']}")
    print(f"  schema : {target['schema'].relative_to(ROOT)}")
    print(f"  example: {target['example'].relative_to(ROOT)}")

    if errors:
        for error in errors:
            path = ".".join(str(p) for p in error.path) or "<root>"
            print(f"[error] {path}: {error.message}")
        raise SystemExit(1)

    print(f"[ok] {target['example'].name} is valid")


def main():
    for target in VALIDATION_TARGETS:
        validate_target(target)


if __name__ == "__main__":
    main()
