def main():
    
    month, day, year = question()
    converter(month, day, year)
    
def converter(m, d, y):
    print(f"{y}-{m:02}-{d:02}")

def question():
    months = [
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
    while True:
        try:
            month, day, year = input("Qual a data: ").split(sep = "/")
            if len(year) != 4:
                pass
            elif int(day) > 31:
                pass
            elif month.isnumeric() == True:
                if int(month) <= 12:
                    return int(month), int(day), int(year)
                else:
                    pass
            elif months.count(month) == 1:
                mon = months.index(month)
                return int(mon)+1, int(day), int(year)
        except:
            pass
        
        
def comletras(m): 
    return month.index(m)
    
    

main()