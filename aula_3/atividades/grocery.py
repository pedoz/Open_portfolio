def main():
    frutas = compras()
    fruli = list(frutas.keys())
    fruli.sort()
    frutasdi = {i: frutas[i] for i in fruli}
    for com in frutasdi:
        print(frutasdi[com], com)


def compras():
    fruit = {}
    x = 1
    while True:
        try:
            item = input("Qual as Frutas:").upper()
            if item in fruit:
                fruit[item] = x + 1
            else:
                fruit[item] = x
            fruit.update()
        except EOFError:
            return fruit


main()