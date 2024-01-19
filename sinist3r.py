import os
from colorama import Fore, Back, Style, init
import requests


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_front_screen():
    clear_screen()
    os.system("title Sinist3r")
    print(f"""{Fore.RED}
                      ╔═╗╦╔╗╔╦╔═{Fore.RESET}╗╔╦╗─┼─┼─╦═╗{Fore.RED}
                      ╚═╗║║║║║╚═{Fore.RESET}╗ ║ ─┼─┼─╠╦╝{Fore.RED}
                      ╚═╝╩╝╚╝╩╚═{Fore.RESET}╝ ╩      ╩╚═{Fore.RED}
          
            Sinist3r - Open sour{Fore.RESET}ced python multitool.
                  {Fore.RED}Live, Laugh, L{Fore.RESET}ove, Sinist3r                        
    """)

def ip_lookup(ip):
    try:
        ip_API = f"http://ipinfo.io/{ip}/json"

        response = requests.get(ip_API)
        jsond_data = response.json()
        
        for key, value in jsond_data.items():
            if key == "readme":
                continue
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error:  {e}")


def start_main():
    show_front_screen()
    while True:
        try:
            rcommand = input(f"{Style.BRIGHT}Sinist3r >> ")
            splittedcommand = rcommand.split(" ")
            command = rcommand.split(" ")[0]
            if command.lower() == "clear" or command.lower() == "cls":
                show_front_screen()
            elif command == "iplookup":
                print("\n")
                ip_lookup(splittedcommand[1])
                print("\n")
            else:
                print("Sinist3r: Command not found")
        except Exception as error:
            print(f"Unexpected error occured (contact sebz0ne): {error}")
            

if __name__ == "__main__":
    start_main()
