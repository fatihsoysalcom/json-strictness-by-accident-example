import json

# This is a valid JSON string according to the JSON standard.
# It uses a single quoted string for a key, which is NOT valid JSON.
# However, some parsers might be lenient and accept it.
# This demonstrates the 'Strict by Accident' concept.

# Example 1: A valid JSON string
valid_json_string = '{\"name\": \"Alice\", \"age\": 30}'

# Example 2: A string that is NOT valid JSON but might be parsed by lenient parsers
# This uses single quotes for the key 'name', which is invalid in strict JSON.
lenient_json_string = "{'name': 'Bob', 'city': 'New York'}"

# Example 3: A string that is valid JSON but might not match application expectations
# This has a trailing comma, which is invalid in strict JSON.
# However, some parsers might accept it.
json_with_trailing_comma = '{\"item\": \"apple\", \"price\": 1.0,}'

print("--- Demonstrating JSON Parsing --- \n")

# Attempt to parse the valid JSON string
try:
    data_valid = json.loads(valid_json_string)
    print(f"Successfully parsed valid JSON: {data_valid}")
except json.JSONDecodeError as e:
    print(f"Error parsing valid JSON: {e}")

print("\n--- Strict by Accident Scenarios ---")

# Attempt to parse the lenient JSON string with Python's strict json module
try:
    # Python's json module is generally strict.
    # This will likely fail because of the single quotes.
    data_lenient = json.loads(lenient_json_string)
    print(f"Parsed lenient JSON (unexpected success): {data_lenient}")
except json.JSONDecodeError as e:
    # This is the expected outcome for a strict parser.
    print(f"Failed to parse lenient JSON (as expected for strict parser): {e}")

# Attempt to parse JSON with a trailing comma
try:
    # Python's json module is generally strict and will reject trailing commas.
    data_trailing_comma = json.loads(json_with_trailing_comma)
    print(f"Parsed JSON with trailing comma (unexpected success): {data_trailing_comma}")
except json.JSONDecodeError as e:
    # This is the expected outcome for a strict parser.
    print(f"Failed to parse JSON with trailing comma (as expected for strict parser): {e}")

print("\nNote: The 'lenient_json_string' and 'json_with_trailing_comma' examples are technically invalid JSON.")
print("A strict JSON parser (like Python's default) will reject them.")
print("However, some parsers might be more forgiving, leading to 'Strict by Accident' scenarios where data seems 'broken' to a strict parser but works elsewhere.")
