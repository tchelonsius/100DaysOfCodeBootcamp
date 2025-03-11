# Day 02: Data Types and more on String Manipulation
# Main project: Tip Calculator
# The project is to create a program that, given the total bill, adds the tip in percentage
# and divides it by the number of people that are going to split, then rounding to two decimal digits.

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12 or 15? ")
people_amount = input("How many people to split the bill? ")

amount_per_person = (int(total_bill)*(1+int(tip)/100))/int(people_amount)
print(f"Each person should pay: ${round(amount_per_person, 2)}")
