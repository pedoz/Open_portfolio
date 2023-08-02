def main():
    frutas = compras()
    for com in frutas:
        print(com)

def compras():
    
    fruit = {}
    while True:
        
        try:
            
            item = input("Qual as Frutas:").upper()
            fruit[item] = len(fruit)
            print(fruit)
            fruit.update()
        except EOFError:
            return fruit


main()