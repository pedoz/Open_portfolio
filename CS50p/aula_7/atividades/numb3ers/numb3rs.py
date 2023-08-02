import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    ip = ip.split(".")
    n = 0
    for i in ip:
        if re.fullmatch(r"[2][0-5][0-5]|[0-1]?[0-9]?[0-9]",i):
            n = n + 1
        else:   
            return "Invalid IP"
    if n == 4:
        return "Valid IP"

if __name__ == "__main__":
    main()