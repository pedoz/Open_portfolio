import re


def main():
    print(convert(input("Hours: ").strip()))

def convert(h):
    if hours := re.fullmatch(r'^((1[0-2]|[1-9]):?(?:[0-5]\d)?) (AM|PM) to ((1[0-2]|[1-9]):?(?:[0-5]\d)?) (AM|PM)$', h):
        inicio = hours.group(1, 3)
        final = hours.group(4, 6)
        if inicio[1] == "PM":
            first = convert_pm(inicio[0])
        else: 
            first = inicio[0]
        if final[1] == "PM":
            second = convert_pm(final[0])
        else: 
            second = final[0]
        first = check_zero(first)
        second = check_zero(second)
        return f"{first} to {second}"
    else:
        raise ValueError("Invalid hour")    

def check_zero(checker):
    if not ":" in checker:
        checker = f"{checker}:00"
    if len(checker) == 4:
        return f"0{checker}"
    else:                
        return checker

def convert_pm(time):
    if ":" in time:
        hour, min = time.split(":")
        hour = int(hour) + 12
        return str(f"{hour}:{min}")
    else:
        time = int(time)
        return str(time + 12)

if __name__ == "__main__":
    main()