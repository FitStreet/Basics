# """Task 2"""

# import json

# with open('task2.json', 'r') as file:
#     json_obj = file.read()
#     python_obj = json.loads(json_obj)
#     print(type(json_obj))
#     print(type(python_obj))
#     print(json_obj)
#     print(python_obj)

"""Task 6"""
# import json
json_products = [{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]

# py_obj = json.loads(json_products)
# print(type(py_obj))
# for i in py_obj:
#     if i["rating"] > 4:
#         print(i["title"])

"""Task 7"""
import json

# with open('db1.json', "x") as file:
#     json.dump(json_products, file, indent= 4)
    
def get_sorted(json_filename: str):
    with open(json_filename) as file:
        py_obj = json.load(file)
        sorted_products = sorted(py_obj, key=lambda x: x.get('rating', 0), reverse=True)
        for i in sorted_products:
            print(i["title"])

    return sorted_products


get_sorted("db1.json")

