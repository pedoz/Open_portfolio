def main():
    month, day, year = question()
    converter(month, day, year)
    
def converter(m, d, y):
    print(f"{y}-{m:02}-{d:02}")

def question():
    while True:
        try:
            month, day, year = input("Qual a data: ").split(sep = "/")
            if len(year) != 4:
                pass
            elif month.isnumeric == True:
                return int(month), int(day), int(year)
            else:
                mon = comletras(month)
                return int(mon)+1, int(day), int(year)
        except:
            pass
        
        
def comletras(m): 
    month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    return month.index(m)
    
    

main()