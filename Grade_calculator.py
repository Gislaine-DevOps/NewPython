# User inputs a grade in his 5 subjects
Math = int(input("Enter your math grade here: "))
Science = int(input("Enter your Science grade here: "))
Social_Studies = int(input("Enter your Social Studies grade here: "))
Language_Arts = int(input("Enter your Language Arts grade here: "))
French = int(input("Enter your French grade here: "))

# Calculate Average Grade
Add = int(Math) + int(Science) + int(Social_Studies) + int(Language_Arts) + int(French)
Average = Add/5

# Determine letter grade
if Average >= 90:
    print(f"Your Average grade is {Average} which is higher than 90. Your grade is an A!")
elif Average >= 80:
    print(f"Your Average grade is {Average} which is higher than 80. Your grade is a B!")
elif Average >= 70:
    print(f"Your Average grade is {Average} which is higher than 70. Your grade is a C")
elif Average >= 60:
    print(f"Your Average grade is {Average} which is higher than 60. Your grade is a D")
else:
    print(f"Your Average grade is {Average} which is lower than a 50. Your grade is an E. You've failed")