#pegar o valor do x e do y
def main():
    question = input("quanto combustível ainda tem? ")
    fuel_perc = convert(question)
    total = gauge(fuel_perc)
    print(f"Fuel left: {total}")

def convert(fraction):
    try:
        x,y = fraction.split(sep="/")
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        else:
            z = x / y
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    else:
        return z * 100
       

def gauge(percentage):
    if 0 <= percentage <= 1:
        return ("E")
    elif percentage > 1 and percentage <= 25:
        return ("25%")
    elif percentage > 25 and percentage <= 50:
        return ("50%")
    elif percentage > 50 and percentage <= 75:
        return ("75%")
    elif percentage > 75 and percentage < 99:
        return ("90%")
    elif percentage >= 99:
        return ("F")
    else:
        return f"erro"


if __name__ == "__main__":
    main()
    