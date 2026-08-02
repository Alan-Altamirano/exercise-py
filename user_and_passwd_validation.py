# Creando una funcion de validacion de usuarios.

stored_users = [
    {"id": 1, "user": "alan2000rc@gmail.com"},
    {"id": 2, "user": "calist20@hotmail.com"},
    {"id": 3, "user": "dylan@gmail.com"},
    {"id": 4, "user": "erik13@hotomail.com.ar"},
]

stored_passwds = [
    {"id": 1, "passwd": "alan"},
    {"id": 2, "passwd": "calist"},
    {"id": 3, "passwd": "dylan"},
    {"id": 4, "passwd": "erik"},
]

enter_user = input("Please enter your user: ").lower().strip()
enter_passwd = input("Plaese enter your password: ")

# Flag variable.
found = False

for user in stored_users:
    if enter_user == user["user"]:
        found = True
        for passwd in stored_passwds:
            if enter_passwd == passwd["passwd"]:
                print("Logging in...")
                break
            else:
                print("Password incorrect, try again")


if not found:
    print("The user is incorrect or does not exist")
