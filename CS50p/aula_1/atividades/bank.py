s = str(input("Como posso te ajudar hoje? ").title())
if str(s).startswith("Hello"):
    print("$0")
elif str(s).startswith("H"):
    print("$20")
else:
    print("$100")