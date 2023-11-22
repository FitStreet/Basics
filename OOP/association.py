# Ассоциация - Принцип ООП, в котором два класса связаны друг с другом. 
# Агрегация - слабая связь 
# Композиция - сильная связь

class Battery:
    _power = 100
    def charge(self):
        self._power = 100

class Iphone:
    def __init__(self, color="black") -> None:
        self.color = color
        self.battery = Battery() # явная связь
        # композиция(сильная связь)
    
    def spend_power(self):
        self.battery._power -= 10

class Nokia:
    def __init__(self, battery:Battery, color="black",) -> None:
        self.color = color
        self.battery = battery


iphone = Iphone("Pink")
battery = Battery()
del iphone # при удалении, удалится и Batte ry
nokia = Nokia(battery, "blue")
del nokia


class Document:
    def __init__(self,content) -> None:
        self.printer = Printer()
        self.content = content

    def print_content(self):
        self.printer.print_document(self)


class Printer:
    def print_document(self, document):
        print("skan")
        content = document.content
        print(content)

document = Document("Hello!")
document.print_content()

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def set_students(self):
        for student in self.students:
            print(student.name)

    def __str__(self) -> str:
        return self.name

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_students(self, student:Student):
        self.students.append(student)

    def get_students(self):
        for student in self.students:
            return student.name

        

math_course = Course('math')
nikita = Student("Nikita", 1)
math_course.add_students(nikita)
print(math_course.get_students())

        


