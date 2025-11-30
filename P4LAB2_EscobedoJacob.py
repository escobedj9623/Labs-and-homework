# P4LAB2_EscobedoJacob.py

run_again = "yes"   # while loop controller

while run_again.lower() == "yes":

    # Ask user for number
    num = int(input("Enter an integer: "))

    # Check for negative
    if num < 0:
        print("Cannot accept negative values.")
    else:
        print(f"\nMultiplication table for {num}:")

        # FOR LOOP → prints table 1 through 12
        for i in range(1, 13):
            result = num * i
            print(f"{num} x {i} = {result}")

    print()  # blank line
    run_again = input("Do you want to run the program again? (yes/no): ")

print("Program ended.")
