from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

def green(text):
    print(Fore.GREEN+text+Style.RESET_ALL, end="")

def yellow(text):
    print(Fore.YELLOW+text+Style.RESET_ALL, end="")

def white(text):
    print(Fore.WHITE+text+Style.RESET_ALL, end="");

def newline():
    print()

colorama_init()

green("t")
yellow("r")
white("a")
green("i")
yellow("l")
newline()