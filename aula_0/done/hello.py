def main():
    hello()
    name = input("What's your name? ").strip().title()
    hello(name)
    
def hello(to = "world"):
    print("Hello,", to)

    
main()