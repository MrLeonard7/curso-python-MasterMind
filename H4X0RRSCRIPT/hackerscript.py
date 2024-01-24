import os


def main():
    desktop_path_linux = "/home/" + os.getlogin() + "/Escritorio/"
    desktop_path_windows = "C:\\Users\\" + os.getlogin() + "\\Desktop\\PARA_TI.txt"
    a = open(desktop_path_linux + "PARA TI.txt", "w")
    a.write("Soy un hacker")
    a.close()


if __name__ == "__main__":
    main()
