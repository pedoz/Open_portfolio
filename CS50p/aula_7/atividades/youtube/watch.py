import re


def main():
    print(parse(input("HTML: ")))

def parse(link):
    if validation :=  re.search(r'src="https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9]+"', link):
        begin, final = validation.group(0).split("/embed/")
        var = final[:-1]
        return f"\nhttps://youtu.be/{var}"
    else:
        return None

if __name__ == "__main__":
    main()