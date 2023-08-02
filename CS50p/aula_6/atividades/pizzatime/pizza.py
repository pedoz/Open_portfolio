from tabulate import tabulate
import csv
import sys

if len(sys.argv) > 2:
    print("Too may command-line arguments")
    sys.exit()
elif len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()
elif not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit()
else:
    filename = sys.argv[1]
    menu = []
    reader = []
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for regular, small, large in reader:
                menu.append({
                            "regular": regular,
                            "small": small,
                            "large": large
                    })
            print(tabulate(menu, tablefmt = "grid"))
            sys.exit()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()