# Jacob Escobedo
# November 7, 2025
# P1HW1 - Math Expressions
# This program asks the user for a base and exponent to calculate powers,
# and then asks for three integers to perform addition and subtraction operations.

# Get base and exponent from user
base = int(input("Enter an integer for the base value: "))
exponent = int(input("Enter an integer for the exponent: "))

# Calculate the result of base raised to the exponent
result = base ** exponent

# Display the result
print()
print(base, "raised to the power of", exponent, "is", result, "!!")

# Get three integers from user
print()
print("Now let's do some addition and subtraction!")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Perform addition and subtraction
sum_result = num1 + num2
final_result = sum_result - num3

# Display the results
print()
print(num1, "+", num2, "=", sum_result)
print(sum_result, "-", num3, "=", final_result)
