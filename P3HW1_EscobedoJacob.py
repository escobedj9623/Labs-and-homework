# ---------------------------------------------------------
# Name: Jacob Escobedo
# Program: P3HW1
# Description:
# This program asks the user to enter six module grades,
# stores them in a list, calculates lowest, highest, sum,
# average, and determines the letter grade.
# ---------------------------------------------------------

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum and average for grades
lowest = min(grades)
highest = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display results
print("\n------------Results------------")
print(f"Lowest Grade: {lowest}")
print(f"Highest Grade: {highest}")
print(f"Sum of Grades: {total}")
print(f"Average: {avg:.2f}")
print("--------------------------------\n")

# Determine letter grade for average
print("------------Grade------------")

if avg >= 90:
    print("Your grade is: A")
elif avg >= 80:
    print("Your grade is: B")
elif avg >= 70:
    print("Your grade is: C")
elif avg >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")

print("--------------------------------")
