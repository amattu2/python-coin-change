# Imports
import sys

# Variables
change = int(sys.argv[1])
coins = {"quarter": 25, "dime": 10, "nickel": 5, "pennies": 1}
usage = {}
result = "The cash register owes:"

# Checks
if (change / coins["quarter"] >= 1):
	# Variables
	amount = int(change / coins["quarter"])
	change = change - (coins["quarter"] * amount)
	usage["quarter"] = amount

	# Debug
	#print(">> Extracted x{0} {1}, which leaves {2}".format(amount, "quarter(s)", change))
if (change / coins["dime"] >= 1):
	# Variables
	amount = int(change / coins["dime"])
	change = change - (coins["dime"] * amount)
	usage["dime"] = amount

	# Debug
	#print(">> Extracted x{0} {1}, which leaves {2}".format(amount, "dime(s)", change))
if (change / coins["nickel"] >= 1):
	# Variables
	amount = int(change / coins["nickel"])
	change = change - (coins["nickel"] * amount)
	usage["nickel"] = amount

	# Debug
	#print(">> Extracted x{0} {1}, which leaves {2}".format(amount, "nickel(s)", change))
if (change / coins["pennies"] >= 1):
	# Variables
	amount = int(change / coins["pennies"])
	change = change - (coins["pennies"] * amount)
	usage["pennies"] = amount

	# Debug
	#print(">> Extracted x{0} {1}, which leaves {2}".format(amount, "pennies", change))

# Output
for key in usage.keys():
	result += " x" + str(usage[key]) + " " + key
print(result if (len(usage.keys()) > 0) else "")
