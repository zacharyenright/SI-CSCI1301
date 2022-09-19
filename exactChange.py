dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

change = int(input())
if change == 0:
    print("No change")
    
dollars = change // 100
if dollars == 1:
    print(dollars, "Dollar")
elif dollars > 1:
    print(dollars, "Dollars")
change = change % 100

quarters = change // 25
if quarters == 1:
    print(quarters, "Quarter")
elif quarters > 1:
    print(quarters, "Quarters")
change = change % 25

dimes = change // 10
if dimes == 1:
    print(dimes, "Dime")
elif dimes > 1:
    print(dimes, "Dimes")
change = change % 10

nickels = change // 5
if nickels == 1:
    print(nickels, "Nickel")
elif nickels > 1:
    print(nickels, "Nickels")

pennies = change % 5
if pennies >= 1:
    print(pennies, "Penny")
elif pennies > 1:
    print(pennies, "Pennies")
