print("Options for toppings of Sandwich are: \n1. Onions\n2. Lettuce\n3. Tomato\n4. Olives\n5. Peppers\n6. Tomatoes\n")


toppingsDict = {
    'Onions': 25,
    'Lettuce': 30,
    'Tomato': 30,
    'Olives': 35,
    'Pepper': 25,
    'Tomatoes': 30
}
print(toppingsDict)
print("Enter 3 types of toppings and enter how many sandwiches you want")
ToppingOne = input("Enter 1st topping: ")
ToppingTwo = input("Enter 2nd topping: ")
ToppingThree = input("Enter 3rd topping: ")
quantity_toppingone = input(f"How many sandwiches of {ToppingOne} you want: ")
quantity_toppingtwo = input(f"How many sandwiches of {ToppingTwo} you want: ")
quantity_toppingthree = input(f"How many sandwiches of {ToppingThree} you want: ")
for keys in toppingsDict.keys():
    if keys == ToppingOne:
        price_one = int(quantity_toppingone) * toppingsDict[keys]
    elif keys == ToppingTwo:
        price_two = int(quantity_toppingtwo) * toppingsDict[keys]
    elif keys == ToppingThree:
        price_three = int(quantity_toppingthree) * toppingsDict[keys]
Total_Price = price_one + price_two +price_three

print(f"The total amount is: {Total_Price}")

