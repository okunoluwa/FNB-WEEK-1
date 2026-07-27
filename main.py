cost = int(input("Cost: R"))
cash = int(input("Cash: R"))

change = cash - cost

denominations = [200, 100, 50, 20, 10, 5, 2, 1]

for denomination in denominations:
    while change >= denomination:
        print(f"R{denomination}")
        change -= denomination