import json

def validate(json_data: str) -> bool:
    try:
        json.loads(json_data)
        return True
    except json.JSONDecodeError:
        return False
