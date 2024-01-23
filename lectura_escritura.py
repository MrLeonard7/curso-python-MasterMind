LISTA_DE_PRODUCTOS_DISPONIBLES = ["Pan", "Pollo", "Pipas"]
SALIDA = "SALIR"
COMANDO_LISTA = "LISTA"


def guardado_de_archivo(lista_compra_usuario):
    nombre_archivo = input("\nQue nombre de archivo le colacaras a tu lista:\n"
                           "->")
    with open(nombre_archivo + ".txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra_usuario))


def preguntar_producto_usuario():
    return input("\nIntroduce un producto [{} para salir]\n"
                 "[{} para lista de productos disponibles]\n"
                 "->".format(SALIDA, COMANDO_LISTA))


def main():
    lista_compra = []

    input_usuario = preguntar_producto_usuario()

    while input_usuario.upper() != SALIDA:
        if input_usuario.upper() == COMANDO_LISTA:
            print("Los productos disponibles son:")
            print("\n".join(LISTA_DE_PRODUCTOS_DISPONIBLES))
            input_usuario = preguntar_producto_usuario()

        elif input_usuario.title() in LISTA_DE_PRODUCTOS_DISPONIBLES:
            lista_compra.append(input_usuario.title())
            print("\nSe ha añadido {}".format(input_usuario.title()))
            print("\n".join(lista_compra))
            input_usuario = preguntar_producto_usuario()

        else:
            print("\n{} no esta disponible en este mommento".format(input_usuario.title()))
            input_usuario = preguntar_producto_usuario()

    guardado_de_archivo(lista_compra)


if __name__ == "__main__":
    main()
