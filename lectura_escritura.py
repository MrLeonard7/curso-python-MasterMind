SALIDA = "SALIR"


def guardado_de_archivo(lista_compra_usuario):
    nombre_archivo = input("\nQue nombre de archivo le colacaras a tu lista:\n"
                           "->")
    with open(nombre_archivo + ".txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra_usuario))


def preguntar_producto_usuario():
    return input("\nIntroduce un producto [{} para salir]\n"
                 "->".format(SALIDA))

def guardar_item_en_lista(input_usuario):
    lista_compra = []
    while input_usuario.upper() != SALIDA:
        if input_usuario.capitalize() not in [a.capitalize() for a in lista_compra]:
            lista_compra.append(input_usuario.capitalize())
            print("\nSe ha añadido {}".format(input_usuario.capitalize()))
            print("\n".join(lista_compra))
            input_usuario = preguntar_producto_usuario()
        else:
            print("\n{} ya esta en la lista.".format(input_usuario.capitalize()))
            input_usuario = preguntar_producto_usuario()

    return lista_compra


def main():
    input_usuario = preguntar_producto_usuario()

    lista_compra = guardar_item_en_lista(input_usuario)

    guardado_de_archivo(lista_compra)


if __name__ == "__main__":
    main()
