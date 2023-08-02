from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    font = figlet.getFonts()

    if len(sys.argv) == 1:
        fonte = random.choice(font)
        figlet.setFont(font = fonte)
        s = question()
        print(figlet.renderText(s))


    elif len(sys.argv) == 3 and sys.argv[1] == ("-f" or "--font"):
        figlet.setFont(font = sys.argv[2])
        s = question()
        print(figlet.renderText(s))


    else:
        sys.exit()


def question():
    s = input("Fale: ")
    return s

main()