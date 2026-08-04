products = ["arroz", "azucar", "yerba", "harina", "sal", "mayonesa"]

for index, product in enumerate(products, start=1):
    print(index, product)

exit_program = False

lista = []
while not exit_program:
    found = False
    search = input("Que producto buscas?: ").lower().strip()
    for product in products:
        if search == product:
            found = True
            lista.append(product)
            print(f"""{product} se agregó exitosamente.
            {lista}""")
            while True:
                question = input("Desea agregar algo mas? si/no: ").lower().strip()
                if question == "no":
                    exit_program = True
                    break
                elif question == "si":
                    break
                else:
                    print("dato invalido")
            break
    if not found:
        print("El producto no se encuentra disponible.")
