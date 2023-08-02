from validator_collection import validators, checkers, errors


def main():
    print(email(input("Your E-mail: ").strip()))

def email(resp):
    try:
        if validators.email(resp):
            username, domain = resp.split("@")
            company, checker = domain.split(".")
            if len(checker) == 3 or len(checker) == 2:
                return "Valid"
            else:
                return "Invalid"
        else:
            return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()