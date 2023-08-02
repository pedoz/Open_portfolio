from datetime import date

tod = str(date.today()).split('-')
res = [int(i) for i in tod]
tod_year, tod_month, tod_day = res


print(tod_year, tod_month, tod_day)



    @classmethod
    def get_born(cls):
        tod = str(date.today()).split('-')
        conv_tod = [int(i) for i in tod]
        tod_year, tod_month, tod_day = conv_tod
        
        try:
            born = input("When you were born? ").split('-')
            conv_born = [int(i) for i in born]
            year, month, day = conv_born
            if (tod_year > year and month > tod_month and tod_day > day) or (year > 2023):