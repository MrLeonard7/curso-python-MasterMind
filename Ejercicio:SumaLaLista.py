
def suma(lista_de_numeros):
    resultado_suma = 0
    for numero in lista_de_numeros:
        resultado_suma = resultado_suma + numero
    return resultado_suma


def main():
    print(suma([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
    