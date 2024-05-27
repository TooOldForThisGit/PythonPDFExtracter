import json

def load_json_to_string(file_path: str) -> str:
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string")

    with open(file_path, 'r') as file:
        json_data = json.load(file)
        json_string = json.dumps(json_data)
        return json_string
    