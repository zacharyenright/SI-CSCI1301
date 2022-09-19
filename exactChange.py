def exact_change(total):
	dollars=0
	quarters=0
	dimes=0
	nickels=0
	pennies=0
	# Calculating number of dollars
	dollars = total // 100
	# Remaining total
	total = total % 100
	# Calculating number of quarters
	quarters = total // 25
	# Remaining total
	total = total % 25
	# Calculating number of dime
	dimes = total // 10
	# Remaining total
	total = total % 10
	# Calculating number of nickels
	nickels = total // 5
	# Remaining total
	pennies = total % 5
	return dollars, quarters, dimes, nickels, pennies


def main():
	cents=int(input())
	dollars,quarters,dimes,nickels,pennies=exact_change(cents)
	if dollars==0 and quarters==0 and dimes==0 and nickels==0 and pennies==0:
		print("No change")
	if dollars==1:
		print(dollars,"Dollar")
	elif dollars>1:
		print(dollars,"Dollars")
	if quarters==1:
		print(quarters,"Quarter")
	elif quarters>1:
		print(quarters,"Quarters")
	if dimes==1:
		print(dimes,"Dime")
	elif dimes>1:
		print(dimes,"Dimes")
	if nickels==1:
		print(nickels,"Nickel")
	elif nickels>1:
		print(nickels,"Nickels")
	if pennies==1:
		print(pennies,"Penny")
	elif pennies>1:
		print(pennies,"Pennies")
  

main()
