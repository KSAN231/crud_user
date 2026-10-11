import json
import sys


def json_load(): #Загрузка JSON
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []

def json_save(users): #Сохранение JSON
    with open("users.json", "w") as file:
        json.dump(users, file, indent=3)

users = json_load()


def get_next_id(users):  # Счетчик count
    if users == []:
        return 1
    numbers = []
    for i in users:
        numbers.append(i["id"])
    count = max(numbers) + 1
    return count

def add_user(users): # Добавление нового пользователя.
    count_id = get_next_id(users)
    add_users = input("Введите имя: ")
    add_age = int(input("Введите возраст: "))
    users.append({
        'id': count_id,
        'name': add_users,
        'age': add_age,
    })
    json_save(users)
    print("Пользователь успешно добавлен.")

def check_users(users): # Просмотр пользователей.
    for user in users:
        print("ID:", (user['id']), "|", "Имя:", (user['name']), "|", "Возраст:", (user['age']))
    if users == []:
        print("Пользователей не существует.")


def train_user(users): # Поиск пользователя по имени.
    train = input("Введите имя пользователя: ")
    found = False
    for user in users:
        if user['name'] == train:
            found = True
            print("ID:", (user['id']), "|", "Имя:", (user['name']), "|", "Возраст:", (user['age']))
    if found == False:
        print("Пользователь не найден.")

def delete_user(users): # Удалить пользователя.
    deleted_id = int(input("Введите ID пользователя: "))
    found = False
    for user in users:
        if user['id'] == deleted_id:
            found = True
            users.remove(user)
            json_save(users)
            print("Пользователь = ID:", (user['id']), "|", "Имя:", (user['name']), "|", "Возраст:", (user['age']), " успешно удален!")
            check_users(users)
    if found == False:
        print("Пользователь не найден.")

def choice_input():
    choice = int(input("_____МЕНЮ_____\n 1.Посмотреть всех пользователей.\n 2.Добавить пользователя.\n 3.Поиск пользователя по имени.\n 4.Удалить пользователя.\n 5.Редактировать пользователя.\n 6.Выход.\n Выбор: "))
    return choice

def redactor_user(users):
    id_search = int(input("Введите ID пользователя: "))
    found = False
    for user in users:
        if user['id'] == id_search:
            found = True
            print("Найден пользователь --- ID:", (user['id']), "|", "Имя:", (user['name']), "|", "Возраст:", (user['age']))
            shift_user = int(input("Что вы хотите изменить?\n 1.Имя\n 2.Возраст\n Введите ответ: "))
            if shift_user == 1:
                new_name = input("Введите новое имя: ")
                user['name'] = new_name
                json_save(users)
            elif shift_user == 2:
                try:
                    new_age = int(input("Введите новые данные возраста: "))
                    user['age'] = new_age
                    json_save(users)
                except ValueError:
                    print("Вы ввели неверные данные, возвращение в главное меню.")
    if found == False:
        print("Пользователь не найден.")



def menu():
    while True:
        try:
            choice = choice_input()
            if choice == 1:
                check_users(users)
            elif choice == 2:
                add_user(users)
            elif choice == 3:
                train_user(users)
            elif choice == 4:
                delete_user(users)
            elif choice == 5:
                redactor_user(users)
            elif choice == 6:
                print("Всего доброго!")
                sys.exit()
            else:
                print("Введенные данные неверны, попробуйте еще раз!")
        except ValueError:
            print("Введенные данные неверны, попробуйте еще раз!")


menu()

