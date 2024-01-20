def es_impar(numero):
    impar = False
    if numero % 2 != 0:
        impar = True
    return impar


def main():
    print(es_impar(24))


if __name__ == "__main__":
    main()
