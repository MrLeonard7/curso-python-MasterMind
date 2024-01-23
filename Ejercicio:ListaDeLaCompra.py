from os import system


def add_list(lista_de_compras, item_para_adicionar):
    if item_para_adicionar in lista_de_compras:
        print("{} ya esta en la lista".format(item_para_adicionar))
    else:
        lista_de_compras.append(item_para_adicionar)

    return lista_de_compras


def main():
    lista_predefinida = ["Leche", "Huevos", "Pan"]
    salida = False

    while not salida:
        system("clear")
        item = input("Que desea agragar a la lista:\n"
                     "->")

        lista_actualizada = add_list(lista_predefinida, item.lower().capitalize())

        print("La lista de compras quedo asi {}".format(lista_actualizada))

        si_no = input("\nDesea agregar otro item al la lista:\n"
                      "(S/N) -> ")

        if si_no.upper() == "S":
            salida = False
            pass
        else:
            salida = True


if __name__ == "__main__":
    main()
