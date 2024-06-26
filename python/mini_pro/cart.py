cart = []
prices = []
total = 0

print("\t\t\t\t WELCOME TO CART")
print()
while True:
    cart_item = input("Enter a item to buy ('Q' for quit): ")
    if cart_item.lower() == "q":
        break
    else:
        price = float(input("Enter the price of a "+cart_item+": ₹"))
        cart.append(cart_item)
        prices.append(price)

print()
print("\t\t\t    ------- YOUR CART ------- ")

for cart_item in cart:
    print(cart_item)

for price in prices:
    total += price

print("Your total is : ₹",total)
print("Thank you for visiting us")