
def main(number):
    number_divisible = []

    for n in range(1, number + 1):
        module = number % n

        if module == 0:
            number_divisible.append(n)

    print("El numero {} es divisible por {}".format(number, number_divisible))

    if len(number_divisible) != 2:
        print("El {} no es primo !!".format(number))
    else:
        print("El {} es primo !!".format(number))


if __name__ == "__main__":
    number = 0

    while number <= 0:
        number = int(input("Ingrese un numero entro positivo:\n"
                           "->"))

    main(number)
