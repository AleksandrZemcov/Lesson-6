def check_admin(login_input, password_input, admins_dict):
    for login, password in admins_dict.items():
        if login == login_input and password == password_input:
            return True  # Пользователь является админом
    return False # Пользователь не является админом


admins = {
    'admin1': 'pass123',
    'admin2': 'qwerty'
}

# Использование функции
user_login = input("Введите логин: ")
user_password = input("Введите пароль: ")

if check_admin(user_login, user_password, admins):
    print("Доступ разрешен. Можно запускать методы управления товарами.")
else:
    print("Нет доступа.")
