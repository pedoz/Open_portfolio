
money = 0
while money < 50:
    x = int(input("quantos pila? "))
    if x == 5:
        money = money + 5
    elif x == 10:
        money = money + 10
    elif x == 25:
        money = money + 25
    
if money == 50:
    print("Aqui está sua coquinha gelada")
else:
    troco = int(money) - 50
    print("Seu troco foi de: ", end = "")
    print(troco, end = ". ")
    print("Aproveite sua coquinha")


