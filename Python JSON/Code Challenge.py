# Import json
import json

# Create a JSON string
x = '{"name": "John", "age": 30}'

# Parse the JSON string
y = json.loads(x)

# Print the age
print(y["age"])