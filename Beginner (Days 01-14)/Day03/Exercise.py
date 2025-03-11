# Exercise: Pizza Order
# The goal of the exercise is to create a program that calculates the end price of the pizza order
# based on its size and the choice on the pepperoni and extra cheese of the client.

print("Welcome to Python Pizza Deliveries!")
size = input("What size? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_price = 0

if size == "S":
    total_price += 15
elif size == "M":
    total_price += 20
elif size == "L":
    total_price += 25
if pepperoni == "Y":
    total_price += 2
if extra_cheese == "Y":
    total_price += 1

print(f"Your final bill is: ${round(float(total_price),2)}")