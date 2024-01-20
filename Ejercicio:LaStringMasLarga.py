
def string_mas_larga(lista_de_strings):
    mas_larga = ""

    for string in lista_de_strings:
        if len(string) > len(mas_larga):
            mas_larga = string
    return mas_larga


def main():
    print(string_mas_larga(["estas", "como", "Hola"]))


if __name__ == "__main__":
    main()