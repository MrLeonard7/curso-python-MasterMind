import string


def amayus(palabra):
    string_mayus = ""

    while len(palabra) != len(string_mayus):
        for letra in palabra:
            contador_minusculas = 0
            for letra_minus in (list(string.ascii_lowercase)):
                contador_minusculas += 1
                if letra == letra_minus:
                    string_mayus += string.ascii_uppercase[contador_minusculas - 1]
    return string_mayus


def main():
    print(amayus("mamahuevo"))


if __name__ == "__main__":
    main()
