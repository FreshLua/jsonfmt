import json

def pretty_format(json_data: str) -> str:
    try:
        parsed = json.loads(json_data)
        return json.dumps(parsed, indent=4)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")

def minify(json_data: str) -> str:
    try:
        parsed = json.loads(json_data)
        return json.dumps(parsed, separators=(",", ":"))
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")
