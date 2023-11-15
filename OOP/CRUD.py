# username
# password
# password_confirn
# email
# запись в бд

import re

{1:['username', '...'], 2:[]}

class RegisterUserMixin:
    __id = 1
    def register(self, username, email, password, password_confirm) -> None: # 
        self.username = username
        self.id = RegisterUserMixin.id
        RegisterUserMixin.id += 1
        self.password = password
        self.password_confirm = password_confirm
        self.email = email
        self._validate_password()
        self._validate_email()
        self.database.update({self.id: [username, email, password]})
    
    def _validate_password(self):
        symbols = "!@#$%^&*+_-~'"
        if not self.password == self.password_confirm:
            raise Exception('Пароли не совпадают')
        if len(self.password) < 8:
            raise Exception ("Пароль должен быть больше 8 символов")
        elif not any(char.isdigit() for char in self.password):
            raise Exception("Password should contain numbers too")
        elif not any(char.isalpha() for char in self.password):
            raise Exception("Password should contain letters as well")
        elif not any(char in symbols for char in self.password):
            raise Exception("Your password should have some symbols")


# regex
# regular expressions
# регулярный выражения
    
    
    def _validate_email(self):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', self.email):
            raise Exception("не правильная почта")
        for v in self.database.values():
            if self.email in v:
                raise Exception("Такая почта уже существует")
            
class LoginUserMixin:
    def login(self, email, password):
        for user_id, user_data in self.database.items():
            if user_data[1] == email and user_data[-1] == password:
                print("успешно залогинились")
                return {'id': user_id,
                       'username': user_data[0],
                         'email': user_data[1]}
        print("не правильная почта или пароль")


class GetUserMixin:
    def retrieve(self, user_id):
        user_data = self.database.get(user_id)
        return {'id': user_id,'username': user_data[0],'email': user_data[1]} if user_data else "Нет такого юзера"

    def listing(self):
            return self.database
    
class DeleteUserMixin:
    def delete(self, user_id):
        user_data = self.database.get(user_id)
        return self.database.pop(user_id) if user_data else "Нет такого юзера"
    

class UpdateUserMixin:
    def update_username(self, user_id, new_username):
        if not user_id in self.database:
            return "Пользователь не найден"
        user_data = self.database.get(user_id)
        user_data[0] = new_username if user_data else user_data
        return {'id': user_id,'username': user_data[0],'email': user_data[1]}

        

    def update_password(self, user_id, new_password):
        if not user_id in self.database:
            return "Пользователь не найден"
        user_data = self.database.get(user_id)
        user_data[0] = new_password if user_data else user_data
        return {'id': user_id,'username': user_data[0],'email': user_data[1]}


class User(
    RegisterUserMixin,
    LoginUserMixin,
    GetUserMixin, 
    DeleteUserMixin, 
    UpdateUserMixin
    ):
    database = {}
           
user = User()
user.register('ff_gg_yy', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
user.register('name_of_user', 'ff1@gmail.com', '12345678!FFd', '12345678!FFd')
ff_data = user.login("ff@gmail.com", '12345678!FFd')

# print(ff_data)
print(user.database)
user.update_username(10,"ivan")
user.update_username(2,"uyt")
print(user.database)
# print(user.listing())
# print(user.retrieve())
# user.delete(1)
# print(user.database)


