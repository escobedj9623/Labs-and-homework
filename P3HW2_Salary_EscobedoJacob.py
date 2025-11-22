# ---------------------------------------------------------
# Name: Jacob Escobedo
# Date: 11/22/2025
# Assignment: P3HW2 Salary
# Description:
# This program asks the user for employee name, hours worked,
# and pay rate. It calculates regular pay, overtime pay,
# and gross pay, then displays all results.
# ---------------------------------------------------------

# PSEUDOCODE (Required)
# Ask user to enter employee name
# Ask user to enter hours worked
# Ask user to enter pay rate
# If hours > 40:
#     overtime hours = hours - 40
#     overtime pay = overtime hours * (payrate * 1.5)
#     regular pay = 40 * payrate
# Else:
#     overtime hours = 0
#     overtime pay = 0
#     regular pay = hours * payrate
# gross pay = regular pay + overtime pay
# Display all results

# INPUT
employee = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))

# CALCULATIONS
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (payrate * 1.5)
    regular_pay = 40 * payrate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours * payrate

gross_pay = regular_pay + overtime_pay

# OUTPUT
print("----------------------------------------------")
print(f"Employee Name: {employee}")
print()
print("Hours Worked:   ", hours)
print("Pay Rate:       ", payrate)
print("Overtime Hours: ", overtime_hours)
print("Overtime Pay:   ", overtime_pay)
print("Regular Pay:    ", regular_pay)
print("----------------------------------------------")
print("Gross Pay:      ", gross_pay)
print("----------------------------------------------")
