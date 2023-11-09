# Миксины - классы расширители, от которых мы наследуемся, от миксинов мы не создаем обекты

class FlyMixin:
    def fly(self):
        print('я могу летать')

class WalkMixin:
    def walk(self):
        print('я могу ходить')
        
class SwimMixin:
    def Swim(self):
        print('я могу Плавать')

class Human(WalkMixin, FlyMixin):
    name = 'человек'
    def talk(self):
        print("я умею говорить")

class Bird(FlyMixin):
    pass

class Fish(SwimMixin):
    pass

class FlyFish(SwimMixin, FlyMixin):
    name = 'flyfish'
    pass


# a = [1,2,3,4,5]
# print(isinstance(a, list))

# print(issubclass(FlyFish, FlyMixin)) # можно узнать наследуется ли класс
flyfish = FlyFish()
print(hasattr(flyfish, "name")) # проверяет находится ли name в flyfish(проверяет находится ли атрибт или метод в классе) True или False

print(getattr(flyfish, 'name')) # находит значение по имени атребута "flyfish"
print(getattr(flyfish, 'nam', 'не найдено')) # не найдено
print(setattr(flyfish, 'name', 5)) # изменяет значение атрибута по названию, если такого атрибута нет, создает его
print(flyfish.__dict__) # выводит все переменные экземпляра класса в виде ключ-значение

#CRUD
# create
# read
# update
# delete


class BornMixin:
    def born(self,name, date):
        self.db_human.update({name.lower():date})

class ShowMixin:
    def show(self, name):
        name = name.lower()
        if name not in self.db_human:
            return 'такого человека не существует'
        for key, value in self.db_human.items():
            if key == name:
                return f"Вот вам {key.title()}, который родился в {value}"

        self.db_human.get(name, 'такого человека не существует')

class UpdateMixin:
    def update_name(self, name, new_name):
        name = name.lower()
        new_name = new_name.lower()
        if name not in self.db_human:
            return 'такого человека не существует'
        value = self.db_human.pop(name)  
        self.db_human[new_name.lower()] = value

class KillMixin:
    def kill(self, name, method_of_murder):
        name = name.lower()
        if name not in self.db_human:
            return 'не нашел'
        self.db_human.pop(name)  
        return f'Успешно был убит {name.title()}, способ убийства: {method_of_murder}'

class CRUD(
    BornMixin,
    ShowMixin,
    UpdateMixin,
    KillMixin
):
    pass


class Human(CRUD):
    db_human = {}
    def __str__(self) -> str:
        return f"{self.db_human}"
        
    
human = Human()
human.born('Nikita', '27-11')
print(human.show('NiKita'))
human.update_name("Nikita", "Tima")
print(human.show('Tima'))
print(human.kill('Tima', "сбила машина и переродился в другом мире"))