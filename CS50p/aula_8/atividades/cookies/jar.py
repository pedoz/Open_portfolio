import sys


class Jar:
    def __init__(self, n):
        self.capacity = n
        self.size = n

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        if n + self.size > self.capacity:
            return ValueError("quale cusao")
        self.size = int(self.size)
        self.size += n
        return self.size

    def withdraw(self, n):
        if n > int(self.size):
            raise ValueError("quale guloso")
        self.size = int(self.size)
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return self._capacity

#tenho que arrumar os erros aqui
    @capacity.setter
    def capacity(self, capacity):
        try:
            if int(capacity) <=0:
                raise ValueError('Not a acceptable number')
        except ValueError:
            raise ValueError("Not a number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def __sub__(self, other):
        cookies = self.size - other.size
        return self.cookies

    def __add__(self, other):
        cookies = self.size + other.size
        return self.cookies

def main():
    jar = Jar(int(input("Qual o tamanho da jarra de cookies? ")))
    while True:
        try:
            question = input("What you want to do now? ")
            if question == "withdraw":
                jar.withdraw(int(input("How many cookies to remove? ")))
            elif question == "deposit":
                jar.deposit(int(input("How many cookies to add? ")))
            elif question == "cookies":
                print(f'{"🍪" * jar.size}')
            elif question == "capacity":
                print(f"{'🍪' * jar.capacity}")
            elif question == "exit":
                print("Cookies in the Jar:\n", jar, sep = "")
                sys.exit()
        except TypeError:
            print(jar)
            sys.exit()

if __name__ == "__main__":
    main()


    # print(jar)
    # wit = jar.withdraw(2)
    # print(wit)
    # print(jar.size)
    # dep = jar.deposit(1)
    # print(dep)
    # print(jar.capacity)
    # print(jar.size)
    # print(jar)
