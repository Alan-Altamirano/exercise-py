# Creando una funcion de validacion de usuarios.

db_users = [
    {"id": 1, "user": "alan2000rc@gmail.com", "passwd": "alan"},
    {"id": 2, "user": "calist20@hotmail.com", "passwd": "calist"},
    {"id": 3, "user": "dylan@gmail.com", "passwd": "dylan"},
    {"id": 4, "user": "erik13@hotmail.com.ar", "passwd": "erik"},
]

enter_user = input("Please enter your user: ").lower().strip()
enter_passwd = input("Plaese enter your password: ")

# Flag variable.
found = False

for user in db_users:
    if enter_user == user["user"]:
        found = True
        if enter_passwd == user["passwd"]:
            print("Logging in...")
            break
        else:
            print("Password incorrect, try again.")


if not found:
    print("The user is incorrect or does not exist, try again.")
