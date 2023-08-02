def main():
    pedido()

def pedido():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0
    while True:
        try:
            order = input("Item: ").title()
            if order in menu:
                print("$", menu[order])
                total = total + float(menu[order])
                print(total)
            else:
                pass
        except EOFError:
            return total

main()