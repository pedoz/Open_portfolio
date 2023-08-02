    @classmethod
    def spl(cls, sub):
        year, month, day = sub.split(',')
        return year, month, day

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self):
        return self._month
    
    @property
    def day(self):
        return self._day
    
    @day.setter
    def day(self):
        return self._day

class Converter(Time):
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.year}/ {self.month}/ {self.day}'



class Converter(Time):
    def __init__(self, time_delta):
        self.time_delta = time_delta

    def convert_to_words(self):
        # your conversion logic here
        pass

def main():
    hoje = Time.get_today()
    born = Time.get_born()
    time_delta = hoje - born
    converter = Converter(time_delta)
    result = converter.convert_to_words()
    print(result)


class Converter(Time):
    def __init__(self, time_delta):
        self.time_delta = time_delta

    def convert_to_words(self):
        years = self.time_delta.year
        months = self.time_delta.month
        days = self.time_delta.day
        # your conversion logic here
        pass