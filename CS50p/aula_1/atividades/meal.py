def main():
    tempo = input("Que horas são:")
    x = convert(tempo)
    if 7 <= x <= 8:
        print("Breakfast time")
    elif 12 <= x <= 13:
        print("Lunch time")
    elif 18 <= x <= 19:
        print("Dinner time")
    else:
        print("No food for you now")


def convert(time):
    #usar no nome que quer splitar o mesmo parametro que exige a função
    horas, minutes = time.split(":")
    new_min = float(minutes) / 60

    #retorna o valor abaixo como o valor de x, ou da váriavel que chamou
    return float(horas) + new_min


if __name__ == "__main__":
    main()
    
    
    
#breakfast time |    lunch time    |  dinner time
#7:00 and 8:00  |  12:00 and 13:00 | 18:00 and 19:00

#relógio em 24-hour time as #:## or ##:##

#Structure your program per the below,
#  wherein convert is a function (that can be called by main)
#  that converts time, a str in 24-hour format, to the corresponding
#  number of hours as a float. For instance, given a time like "7:30"
#  (i.e., 7 hours and 30 minutes), convert should return 7.5 
# (i.e., 7.5 hours).