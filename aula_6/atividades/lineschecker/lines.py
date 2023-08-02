import sys

if len(sys.argv) > 2:
    print("Too may command-line arguments")
    sys.exit()
elif len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()
elif not sys.argv[1].endswith(".py"):
    print("Not a Python file")
    sys.exit()
else:
    filename = sys.argv[1]
    final_list =[]
    try:
        with open(filename) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

for line in lines:
    line = line.strip()
    if not (line.startswith("#") or line == ""):
        final_list.append(line)
    else:
        pass

num_lines = len(final_list)
print(f"{filename} has {num_lines} lines.")