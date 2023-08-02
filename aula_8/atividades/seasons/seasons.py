from datetime import date
import sys
import inflect


class Time:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.year},{self.month},{self.day}'

    @classmethod
    def get_today(cls):
        hoje = str(date.today())
        year, month, day = hoje.split("-")
        return cls(int(year),int(month),int(day))

    @classmethod
    def get_born(cls):
        try:
            born = input("When you were born? ").split('-')
            converted_born = [int(i) for i in born]
            year, month, day = converted_born
            if year > 2023:
                sys.exit()
            return cls(year, month, day)
        except ValueError:
            sys.exit()

    def __sub__(self, other):
        year = self.year - other.year
        month = self.month - other.month
        day = self.day - other.day
        return Time(year, month, day)

    @classmethod
    def converter(cls, hoje, born):
        total = hoje - born
        dated = str(total).split(',')
        dated_int = [int(i) for i in dated]
        y, m, d = dated_int
        bis_y = int(y / 4)
        m = m + y * 12
        d = d + m * 24
        h = d * 24
        minutes = (h * 60) + (bis_y * 1660)
        p = inflect.engine()
        words = p.number_to_words(minutes, andword='')
        return f'{words}'
        

def main():
    hoje = Time.get_today()
    born = Time.get_born()
    tot = Time.converter(hoje, born)
    print(tot)    

if __name__ == "__main__":
    main()


