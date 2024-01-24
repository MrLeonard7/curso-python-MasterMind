SALIDA = "SALIR"
NOMBRE_ARCHIVO_LISTA = "Lista Compra.txt"


def guardado_de_archivo(lista_compra_usuario):
    with open(NOMBRE_ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra_usuario))


def preguntar_producto_usuario():
    return input("\nIntroduce un producto [{} para salir]\n"
                 "->".format(SALIDA))


def guardar_item_en_lista(input_usuario,lista_compra):
    if input_usuario.capitalize() not in [a.capitalize() for a in lista_compra]:
        lista_compra.append(input_usuario.capitalize())
        print("\nSe ha añadido {}".format(input_usuario.capitalize()))

    else:
        print("\n{} ya esta en la lista.".format(input_usuario.capitalize()))

def cargar_o_crear_lista():
    lista_compra = []

    if input("¿Quieres cargar la ultima lista de la compra? [S/N]\n"
             "->").upper() == "S":
        try:
            with open(NOMBRE_ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("¡Archivo de la compra no encontrado!")
    return lista_compra


def mostrar_lista(lista_compra):
    print("\nTu lista es:\n" + "\n".join(lista_compra))


def main():
    lista_compra = cargar_o_crear_lista()
    mostrar_lista(lista_compra)
    input_usuario = preguntar_producto_usuario()

    while input_usuario.upper() != SALIDA:
        guardar_item_en_lista(input_usuario, lista_compra)
        input_usuario = preguntar_producto_usuario()

    mostrar_lista(lista_compra)
    guardado_de_archivo(lista_compra)


if __name__ == "__main__":
    main()
