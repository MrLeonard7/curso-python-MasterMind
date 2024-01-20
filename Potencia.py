from math import pow


def lista_de_string_a_entero(lista):
    lista_limpia = []
    for n in lista:
        n_limpio = int(n)
        lista_limpia.append(n_limpio)

    return lista_limpia


def potencia(numero, *elevado):
    if elevado:
        return pow(numero, elevado[0])

    return pow(numero, 2)


def main():
    n = input("Coloca primero el numero del que quieras hacer la potencia\n"
              "y luego el numero al que lo quieras elevar separados por una coma\n"
              "si no colocas sera elevado al cuadrado\n"
              "->").split(",")
    if len(n) == 2:
        n = lista_de_string_a_entero(n)
        print(potencia(n[0], n[1]))
    else:
        n = int(n[0])
        print(potencia(n))


if __name__ == "__main__":
    main()
