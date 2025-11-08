import json

def load_json_file_safely(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied reading '{filepath}'")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{filepath}'")
        print(f"  {e.msg} at line {e.lineno}")
        return None

data = load_json_file_safely('missing_file.json')
if data is None:
    print("Using default configuration")
    data = {"timeout": 30, "retries": 3}