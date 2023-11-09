# Наследование - принцип ООП, в котором мы можем унаследовать, переопределить, и использовать в дочернем классе все методы и атрибуты родительского класса.
#object - класс прородитель,  от которого наследуются все классы (в котором хранятся все магичиские методы)
class A:
    h = 5
    def method(self):
        print('method A')

a = A() # 5
# a.method() # method A

class B(A): # класс B наследует класс А (указывам классы от которых хотим унаследоватся)
    h = 6
    def method(self):
        super().method() # если мы хотим обратится к методам родительского класса
        print('method B')

class C(B, A):
    pass

b = B()
# b.method() # method B
b.h # 6


class Human:
    def __init__(self, name, age, sex) -> None:
        self.name= name
        self.age = age
        self.sex = sex

    def get_info(self):
        return f"My name is {self.name}, I'm {self.age} years old"
    

class Student(Human):
    def __init__(self, name, age, sex, facultet, kurs) -> None:
        super().__init__( name, age, sex)
        self.facultet = facultet
        self.kurs = kurs

    def get_info(self):
        return super().get_info() + f", I'm styding at {self.facultet} on {self.kurs} course"


student1 = Student('Nikita', 20, "Male", 'IT', 3)
# print(student1.get_info())
# print(super(Student, student1).get_info())

# все классы по дефолту наследуются от object
# одиночное наследование
class A:
    pass
# множественное наследование
# многоуровневое наследование
class B(A):
    pass
# иерархическое наследование
class A:
    pass
class B(A):
    pass
class C(A):
    pass
# гибридное наследование

# MRO - method resolution order. Решает проблему ромба(ищет в глубину потом в ширину)
#    A
#  /   \
# B     C
#  \   /
#    D

class A:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name + "str"
    
    def __repr__(self) -> str:
        return self.name + "repr"

a = A('Tima')
print(a)

# найти отличие __str__ | __repr__
# Самое важное отличие между __str__ и __repr__ заключается в их целях и назначении:

# __str__ предназначен для представления объекта в удобочитаемой форме для человека.
#__repr__ предназначен для представления объекта в форме, которая может быть использована для воссоздания (восстановления) объекта с теми же параметрами.
#Ключевая идея заключается в том, что __str__ предназначен для человеческого потребления, в то время как __repr__ предоставляет информацию, которая полезна при работе с кодом и отладке. Выбор между ними зависит от того, для какой цели вы хотите представить объект в виде строки.
# len 12345678
# yield

class IterInt(int):
    def __iter__(self): 
        for i in str(self):
            yield int(i) # оператор для генерирования 

a = IterInt(123456789)
for i in a:
    print(i)
        


