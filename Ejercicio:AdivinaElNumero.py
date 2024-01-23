from random import randint
from os import system

def adivina_el_numero(n_desde, n_hasta):
    has_adivinado = False
    numero_ganador = randint(n_desde, n_hasta)
    while not has_adivinado:
        system("clear")
        numero_usuario = int(input("Elija el numero ganador entre {} y {}\n"
                                   "->".format(n_desde, n_hasta)))
        if numero_ganador == numero_usuario:
            has_adivinado = True
            return numero_ganador
        else:
            print("\nEl {} no es el verdadero".format(numero_usuario))
            input("Sigue intentando presiona enter...")



def main():
    eleccion = []
    while len(eleccion) != 2:
        eleccion = input("Escriba un rango de numeros entre 1 a 100 y luego adivina el numero ganador\n"
                         "Escribe los dos numeros separados por una coma: \n"
                         "->").split(",")
    n = 0
    for numero in eleccion:
        numero = int(numero)
        eleccion[n] = numero
        n += 1

    adivina = adivina_el_numero(eleccion[0], eleccion[1])

    print("Felidades el numero ganador si era {} !!!".format(adivina))


if __name__ == "__main__":
    main()
