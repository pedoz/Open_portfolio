oper = input("Qual a operação? ")
ox, oy, oz = oper.split(" ")

x = int(ox)
z = int(oz)

if oy == "+":
    print(x + z)
elif oy == "-":
    print(x - z)
elif oy == "/":
    print(x / z)
elif oy == "*":
    print(x * z)
else:
    print("deu erro")