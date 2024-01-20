
def fibonacci(n_terminos):
    n1 = 0
    n2 = 1
    terminos_fibonacci = [n1]

    for n in range(n_terminos):
        suma = n1 + n2

        terminos_fibonacci.append(suma)

        n2 = n1
        n1 = suma
    return terminos_fibonacci


def main():
    n = int(input("¿Cuantos terminos quiere conocer de fibonacci?"))
    print(fibonacci(n))


if __name__ == "__main__":
    main()
