#pegar o valor do x e do y
def main():
    fuel_perc = convert()
    total = gauge(fuel_perc)
    print(f"Fuel left: {total}")

def convert():
    while True:
        x, y = input("quanto combustível ainda tem? ").split(sep="/")
        if 0 < x <= 100 and 0 < y <= 100:
            try:
                fuel = int(x) / int(y)
                if fuel > 1:
                    pass
                else:
                    return fuel
            except (ValueError, ZeroDivisionError):
                pass
        else:
            pass

def gauge(percentage):
    if percentage <= 0.01:
        return ("E")
    elif percentage > 0.01 and percentage <= 0.25:
        return ("25%")
    elif percentage > 0.25 and percentage <= 0.50:
        return ("50%")
    elif percentage > 0.50 and percentage <= 0.75:
        return ("75%")
    elif percentage > 0.75 and percentage < 0.99:
        return ("90%")
    elif percentage >= 0.99:
        return ("F")


if __name__ == "__main__":
    main()
    