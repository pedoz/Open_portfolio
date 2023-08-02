#pegar o valor do x e do y
def main():
    fuel = get_fuel()
    total = fuel_left(fuel)
    print(f"Fuel left: {total}")

def get_fuel():
    while True:
        x, y = input("quanto combustível ainda tem? ").split(sep="/")
        try:
            fuel = int(x) / int(y)
            if fuel > 1:
                pass
            else:
                return fuel
        except (ValueError, ZeroDivisionError):
            pass

def fuel_left(t):
    if t <= 0.01:
        return ("E")
    elif t > 0.01 and t <= 0.25:
        return ("25%")
    elif t > 0.25 and t <= 0.50:
        return ("50%")
    elif t > 0.50 and t <= 0.75:
        return ("75%")
    elif t > 0.75 and t < 0.99:
        return ("90%")
    elif t >= 0.99:
        return ("F")



main()
    