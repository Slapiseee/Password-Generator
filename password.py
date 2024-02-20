import random
import string
import subprocess
from colorama import Fore as banner, init
import time

init()

banner = f"""{banner.RED}
▄▀▀▄ ▄▀▄  ▄▀▀█▄▄   ▄▀▀▄▀▀▀▄      ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄ 
█  █ ▀  █ █ ▄▀   █ █   █   █     █        ▐  ▄▀   ▐ █  █ █ █ ▐  ▄▀   ▐ █   █   █ ▐ ▄▀ ▀▄ █    █  ▐ █      █ █   █   █ 
▐  █    █ ▐ █    █ ▐  █▀▀▀▀      █    ▀▄▄   █▄▄▄▄▄  ▐  █  ▀█   █▄▄▄▄▄  ▐  █▀▀█▀    █▄▄▄█ ▐   █     █      █ ▐  █▀▀█▀  
  █    █    █    █    █          █     █ █  █    ▌    █   █    █    ▌   ▄▀    █   ▄▀   █    █      ▀▄    ▄▀  ▄▀    █  
▄▀   ▄▀    ▄▀▄▄▄▄▀  ▄▀           ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   ▄▀   █    ▄▀▄▄▄▄   █     █   █   ▄▀   ▄▀         ▀▀▀▀   █     █   
█    █    █     ▐  █             ▐         █    ▐   █    ▐    █    ▐   ▐     ▐   ▐   ▐   █                  ▐     ▐   
▐    ▐    ▐        ▐                       ▐        ▐         ▐                          ▐                            
{banner.RESET}"""

def password_generator(length):
    """Generates a random and secure password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def clear_screen():
    """Clears the screen."""
    print("\033[H\033[J")

def restart():
    """Clears the screen and prompts the user to restart the program."""
    clear_screen()
    print(banner + "\n" * 3)

    while True:
        clear_screen()
        print(banner + "\n" * 3)
        arg = input("Do you want to generate another password? [Yes/No] ").strip().lower()
        if arg in ("yes", "no"):
            break
        clear_screen()
        print(banner + "\n" * 3)
        print("Invalid input. Please enter 'Yes' or 'No'.")
        time.sleep(2)

    if arg == "yes":
        clear_screen()
        print(banner + "\n" * 3)
    else:
        exit()

while True:
    """Generates a password, stores it in a text file, and opens the file with Notepad."""
    clear_screen()
    print(banner + "\n" * 3)
    length = int(input("Enter the desired length for the password: "))

    password = password_generator(length)

    with open("password.txt", "w") as file:
        file.write(password + "\n")
        print("Your password has been generated successfully")

    subprocess.Popen(["notepad.exe", "password.txt"])
    
    time.sleep(3)
    restart()
