import random
import string
import subprocess
from colorama import *
import time
import os


banner = f"""{Fore.RED}
▄▀▀▄ ▄▀▄  ▄▀▀█▄▄   ▄▀▀▄▀▀▀▄      ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄ 
█  █ ▀  █ █ ▄▀   █ █   █   █     █        ▐  ▄▀   ▐ █  █ █ █ ▐  ▄▀   ▐ █   █   █ ▐ ▄▀ ▀▄ █    █  ▐ █      █ █   █   █ 
▐  █    █ ▐ █    █ ▐  █▀▀▀▀      █    ▀▄▄   █▄▄▄▄▄  ▐  █  ▀█   █▄▄▄▄▄  ▐  █▀▀█▀    █▄▄▄█ ▐   █     █      █ ▐  █▀▀█▀  
  █    █    █    █    █          █     █ █  █    ▌    █   █    █    ▌   ▄▀    █   ▄▀   █    █      ▀▄    ▄▀  ▄▀    █  
▄▀   ▄▀    ▄▀▄▄▄▄▀  ▄▀           ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   ▄▀   █    ▄▀▄▄▄▄   █     █   █   ▄▀   ▄▀         ▀▀▀▀   █     █   
█    █    █     ▐  █             ▐         █    ▐   █    ▐    █    ▐   ▐     ▐   ▐   ▐   █                  ▐     ▐   
▐    ▐    ▐        ▐                       ▐        ▐         ▐                          ▐                            
{Fore.RESET}"""

def generateur_mdp(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longueur))

def restart():
    os.system("cls")
    print(banner + "\n" * 3)
    arg = input("Voulez-vous créer un autre mot de passe ? [Oui/Non] ").strip().lower()
    if arg == "oui":
        os.system("cls")
        print(banner + "\n" * 3)
        return True
    else:
        exit()


while True:
    os.system("cls")
    print(banner + "\n" * 3)
    longueur = int(input("Entrez la longueur souhaitée pour le mot de passe : "))

    mdp_generé = generateur_mdp(longueur)

    with open("password.txt", "a+") as file:
        file.write(mdp_generé + "\n")
        print("Votre mot de passe a bien été généré")

    subprocess.Popen(["notepad.exe", "password.txt"])
    
    time.sleep(3)
    restart()