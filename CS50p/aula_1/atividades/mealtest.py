while True:
    tempo = input("que horas sâo?")
    horas, minutos = tempo.split(":")
    if int(minutos) <= 60:
        break

print (horas + minutos)




def main():
    time()
    convert()


def convert():
    horas, minutos
    print(horas)
    print(minutos)
    

def time():
    while True:
        tim = input("que horas são: ")
        horas, minutos = tim.split(":")
        if int(minutos) <= 60:
            break
        return horas, minutos

main()