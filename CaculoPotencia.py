import math
import os


def main(number):

    pow_number = math.pow(number, 2)

    return pow_number


if __name__ == "__main__":

    number_user = None

    while number_user != 0:
        number_user = int(input("Ingrese un numero:\n"
                                "->"))

        power = main(number_user)

        print("la potencia de {} es {}".format(number_user, power))

        input("Presione Enter para ingresar otro numero")
        os.system("clear")
    