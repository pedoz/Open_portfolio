def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    elif len(s) < 4 or len(s) > 7:
        return False
    elif s[0].isdigit() or s[1].isdigit():
        return False
    elif s[-1].isalpha() or s[-2].isalpha():
        return False 
    else:
        ls = list(s)  
        for i in range(len(ls)):
            if ls[i].isdigit():
                if ls[i] == '0':
                    return False
                elif i < len(ls) -1 and ls[i+1].isalpha():
                    return False
                else:
                    return True
            
if __name__ == "__main__":
    main()
