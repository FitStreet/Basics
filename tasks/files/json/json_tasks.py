"""Task 2"""

import json

with open('task2.json', 'r') as file:
    json_obj = file.read()
    python_obj = json.loads(json_obj)
    print(type(json_obj))
    print(type(python_obj))
    print(json_obj)
    print(python_obj)