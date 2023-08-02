menu = [
    {"name" : "Baja Taco", "value" : 4.00},
    {"name" : "Burrito", "value" : 7.50},
    {"name" : "Bowl", "value" : 8.50},
    {"name" : "Nachos", "value" : 11.00},
    {"name" : "Quesadilla", "value" : 8.50},
    {"name" : "Super Burrito", "value" : 8.50},
    {"name" : "Super Quesadilla", "value" : 9.50},
    {"name" : "Taco", "value" : 3.00},
    {"name" : "Tortilla Salad", "value" : 8.00}
]

order = input("Item: ").title()
if order(menu["name"]) == True:
    print(order)


#
# 
# 
# for food in menu:
    print(food["name"], food["value"], sep = ": $")