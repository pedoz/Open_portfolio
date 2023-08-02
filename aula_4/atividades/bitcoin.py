import sys
import requests
import json

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()
try:
    bit = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()
else:
    try:
        site = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        print("deu erro no site")
        sys.exit()
    else:
        data = site.json()
        coun = data["bpi"]
        usd = coun["USD"]
        value = usd["rate"]
        usd_rate = float(usd["rate_float"])
        custo = bit * usd_rate

print(f"${custo:,.4f}") 