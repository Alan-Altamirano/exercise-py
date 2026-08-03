# menu interactivo
print("======== Welcome =========")
print("A continuacion inicie sesion")

db_users = [
    {"id": 1, "user": "admin@corp.com", "password": "admin"},
    {"id": 2, "user": "rrhh@corp.com", "password": "rrhh"},
    {"id": 3, "user": "employee@corp.com", "password": "employee"},
]


enter_user = input("Enter your user: ").lower().strip()
enter_passwd = input("Enter your password: ")

found = False

for user in db_users:
    if enter_user == user["user"]:
        found = True
        if enter_passwd == user["password"]:
            print("Iniciando sesion...")
            break
        else:
            print("La contraseña es incorrecta, intentelo otra vez.")

if not found:
    print("El usuario es incorrecto o no exite")
