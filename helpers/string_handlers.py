import json

def clean_chars_from_string(str_to_clean, *chars_to_remove):
    
    if not isinstance(str_to_clean, str):
        raise ValueError("The first argument must be a string representing the JSON data.")
    
    for char in chars_to_remove:
        if not isinstance(char, str) or len(char) < 1:
            raise ValueError("Each character to remove must be a non-empty string.")
    
    for char in chars_to_remove:
        output_str = str_to_clean.replace(char, '')
    return output_str

def extract_json_object(input_str):
    if not isinstance(input_str, str):
        raise ValueError("The input must be a string representing the JSON data.")
    
    start_index = input_str.find('{')
    end_index = input_str.rfind('}')
    
    if start_index == -1 or end_index == -1 or start_index >= end_index:
        raise ValueError("The input does not contain a valid JSON object enclosed in curly braces.")
    
    json_str = input_str[start_index:end_index + 1]
    
    try:
        json_obj = json.loads(json_str)
    except json.JSONDecodeError:
        raise ValueError("The extracted JSON string is not a valid JSON object.")

    
    return json_obj