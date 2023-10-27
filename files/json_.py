"===================JSON=============="
# JSON - Java Script Object Notation - универсальный формат, в котором мы можем хранить какие то данные в типах данных, понятных для многих языков програмирования.
{
    "name":"Ivan"
}
import json

"""==================DUMP DUMPS"""
# сериализация - перевод в формат JSON
# DUMPS - переводит данные в json(переводит сначала в str)
# DUMP - принимает в себя данные и файл, чтобы записать эти данные в наш файл в формат json
# list_ = [1,2,3,4,5]
# data = {
#     'name':'Nikita',
#     'last_name':'Grebnev'
# }
# print(type(list_)) # <class 'list'>
# list_ = json.dumps(list_)
# print(type(list_)) # <class 'str'>

# file = open('data.json', 'w')
# json.dump(data, file)
# file.close()
# with open("data.json", 'w') as file:
#     file.write(list_)



"""==================LOAD LOADS"""
# Десериализация - перевод из json в python
# LOAD принимает файл и переводит этот файл из Json в Python. 
# LOADS переводит данные из json в python(можно заменить eval())
with open('data.json', 'r') as file:
    data = file.read()
    print(type(data))
    # data = json.loads(data)
    data = eval(data)
    print(type(data))

# list_ = json.loads(list_)
# print(type(list_))

data = "10+10"
eval(f"print({data})") 

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)


# CVS как записывать и как получать данные