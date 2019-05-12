from random import randrange
import colorama
from colorama import Fore
from colorama import Style

def hack():
    if randrange(2):
        print(Fore.GREEN + "HACKED SUCCESSFULLY")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED + "HACKING FAILED.")
        print("YOU ARE NOW ON A LIST.")
        print("CALLING 0118 999 881 999 119 725... 3")
        print(Style.RESET_ALL)
