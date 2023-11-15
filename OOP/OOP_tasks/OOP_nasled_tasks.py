"""Task 3"""
class MyString(str):
    def __init__(self, string) -> None:
        self.string = string

    def append(self, word):
        self.word = word
        self.string = self.string + word
        return self.string
    
    def pop(self):
        last_s = self.string[-1]
        self.string = self.string[:-1]
        return last_s
        
    
    def __str__(self): 
        return self.string
    
example = MyString('String') 
# example.append('hello') 
# print(example.pop()) 
# print(example) 

"""Task 5"""

class Person: 
    def __init__(self, name, age): 
        self.name = name  
        self.age = age

    def display(self):
        print(f"name:{self.name}, age:{self.age}")

class Student(Person):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty

    def display_student(self):
        print(f"name:{self.name}, age:{self.age}, faculty:{self.faculty}")

obj_student = Student("Rick", 21, "science")

# obj_student.display() 
# obj_student.display_student()

"""Task 7"""

class SmartPhones:
    def __init__(self, name, color, memory, battery = 0) -> None:
        self.name = name
        self.color = color
        self.memory = memory
        self.battery = battery

    def __str__(self) -> str:
        return f"{self.name} {self.memory}"
    
    def charge(self, number):
        self.battery += number


class Iphone(SmartPhones):
    
    def __init__(self, name, color, memory, ios, battery=0) -> None:
        super().__init__(name, color, memory, battery)
        self.ios = ios

    def send_imessage(self, message):
        return f"sending {message} from {self.name} {self.memory}"


class Samsung(SmartPhones):
    def __init__(self, name, color, memory, android, battery=0) -> None:
        super().__init__(name, color, memory, battery)
        self.android = android

    def show_time(self):
        from datetime import datetime
        current_date_time = datetime.now()
        current_time = current_date_time.time()
        return current_time


phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) 

print(phone.battery) 
phone.charge(20) 
print(phone.battery) 

iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 

samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time()) 



