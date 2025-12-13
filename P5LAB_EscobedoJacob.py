# Jacob Escobedo
# December 13, 2025
# P5LAB - Self Checkout Change Dispenser
# This program simulates a self-checkout machine and displays change using coins.

import random

def disperse_change(change):
    change = round(change, 2)

    dollars = int(change // 1)
    change = round(change - dollars, 2)

    quarters = int(change // 0.25)
    change = round(change - quarters * 0.25, 2)

    dimes = int(change // 0.10)
    change = round(change - dimes * 0.10, 2)

    nickels = int(change // 0.05)
    change = round(change - nickels * 0.05, 2)

    pennies = int(round(change / 0.01))

    if dollars > 0:
        print(f"Dollars: {dollars}")
    if quarters > 0:
        print(f"Quarters: {quarters}")
    if dimes > 0:
        print(f"Dimes: {dimes}")
    if nickels > 0:
        print(f"Nickels: {nickels}")
    if pennies > 0:
        print(f"Pennies: {pennies}")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")

    cash_given = float(input("Enter cash amount: $"))

    if cash_given < total_owed:
        print("Not enough money entered.")
    else:
        change = round(cash_given - total_owed, 2)
        print(f"Change owed: ${change:.2f}")
        disperse_change(change)

main()
