camelCase = input("CamelCase: ")
print("snake_case:", end="")

for letra in camelCase:
    if letra.isupper():
        print("_" + letra.lower(), end="")
    else:
        print(letra, end="")