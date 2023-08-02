def main():
    twttr = input("Fala ai: ")
    print(shorten(twttr))    


def shorten(word):
    
    result = ""
    
    for letra in word:
        if not letra in ["a", "e", "i", "o", "u"]:
            result = result + letra


    return result

if __name__ == "__main__":
    main()