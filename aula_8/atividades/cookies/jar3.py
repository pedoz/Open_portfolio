class Jar:
    def __init__(self, capacity=12) -> None:
        self.capacity = capacity
        self.size = 0

    def __str__(self) -> str:
        return f"{'🍪'*self.size}"

    def deposit(self, n: int) -> None:
        self.size += n

    def withdraw(self, n: int) -> None:
        self.size -= n

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self,capacity: int) -> None:
        if capacity < 0:
            raise ValueError("Invalid capacity of the jar")
        self._capacity = capacity

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self,size: int) -> None:
        if size < 0:
            raise ValueError("Too few cookies")
        if size > self.capacity:
            raise ValueError("Too many cookies")
        self._size = size


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