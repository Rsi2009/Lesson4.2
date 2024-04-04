class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = "user"

    def get_user_id(self):
        return self._user_id

    def get_user_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def get_user_info_str(self):
         return f"{self._user_id}: {self._name}"

    def __str__(self):
        return f"{self._user_id}: {self._name}, Access Level: {self._access_level}"
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = "admin"
        self._users_list = []


    def add_user(self, user):
        self._users_list.append(user)
        print(f"сотрудник {user.get_user_info_str()} добавлен в список сотрудников")

    def remove_user(self, user):
        if user in self._users_list:
            self._users_list.remove(user)
            print(f"сотрудник {user.get_user_info_str()} удален из списка сотрудников")
        else:
            print(f"сотрудник {user} не найден в списке сотрудников")
    def get_users(self):
        return self._users_list[:]


    def get_users_names(self):
         a = []
         for user in self._users_list:
             a.append(user._name)
         return a

user1 = User(1, "Марина")
user2 = User(2, "Олег")
admin = Admin(3, "Александр")

print(user1.get_user_info_str())
print(user2.get_user_info_str())
print(admin.get_user_info_str())

user4 = User(4, "Виктор")
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user4)
admin.add_user(admin)
print(admin.get_users())
print(admin.get_users_names())

admin.remove_user(user2)
print(admin.get_users())
print(admin.get_users_names())
