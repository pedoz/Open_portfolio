def main():
    question = str(input("Como posso te ajudar hoje? ").lower())
    print(value(question))
    


def value(greeting):
    if str(greeting).startswith("hello"):
        return f"$0"
    elif str(greeting).startswith("h"):
        return f"$20"
    else:
        return f"$100"


if __name__ == "__main__":
    main()