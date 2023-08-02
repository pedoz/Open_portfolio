twtter = input("Fala ai: ")
for letras in twtter:
    if not letras in ["a", "e", "i", "o", "u"]:
        print(letras, end="")