# Input: Get user's body weight in pounds
weight_in_lbs = float(input("Enter your weight in pounds: "))

#Convert weight in lbs to kg, knowing that 1lbs is equal to approximately 0.453592
weight_in_kg = float(weight_in_lbs) * 0.453592

#Result in kilograms
print(f"Your weight in kilograms is {weight_in_kg:.3f}")