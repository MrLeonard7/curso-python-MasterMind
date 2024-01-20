
def estas_seguro(respuesta=None):
    if respuesta == "Y":
        respuesta = True
    elif respuesta == "N":
        respuesta = False

    return respuesta


def main():

    seguro = input("Estas seguro (Y/N)")

    print(estas_seguro(seguro))


if __name__ == "__main__":
    main()
