

def medir_lagos(iterable, *args, sumar_largos=False):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        if sumar_largos:
            largos = sum(largos)
        return largos
    return len(iterable)


def suma(*args):
    return sum(args)


def main():
    print(medir_lagos("hola"))
    print(medir_lagos("hola", "como", "estas", sumar_largos=True))
    print(suma(1, 2, 3, 4, 3, 5))


if __name__ == "__main__":
    main()
