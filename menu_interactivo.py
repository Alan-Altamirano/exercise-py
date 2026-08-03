# menu interactivo
print("\t\t ======== Welcome back! =========")
print("\t\t Log in to continue\n")

db_users = [
    {"id": 1, "user": "admin@corp.com", "password": "admin"},
    {"id": 2, "user": "rrhh@corp.com", "password": "rrhh"},
    {"id": 3, "user": "employee@corp.com", "password": "employee"},
]

cut = False

while not cut:
    enter_user = input("Enter your user: ").lower().strip()
    enter_passwd = input("Enter your password: ")
    
    found = False
    
    for user in db_users:
        if enter_user == user["user"]:
            found = True
            if enter_passwd == user["password"]:
                cut = True
                print("Logging in...")
                break
            else:
                print("The password is incorrect. Please try again")
    
    if not found:
        print("User not found")


print("Loggin successful.\n")

running = False

while not running:
    
    print("MENU")
    print("""
    a_Load new order
    b_view order
    c_Modify order
    d_Delete order
    e_view detail order
    """)
    option = input("Select an option: ").lower().strip()

    if option == "a":
        print("done")
    elif option == "b":
        print("done")
    elif option == "c":
        print("done")
    elif option == "d":
        print("done")
    elif option == "e":
        print("done")
    else:
        running = True
        print("exit")

        