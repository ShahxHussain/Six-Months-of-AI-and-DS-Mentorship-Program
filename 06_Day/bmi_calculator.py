# Ask for the user's name
name = input("Enter your name: ")

# Ask for the user's weight in kilograms
weight = float(input("Enter your weight in kilograms: "))

# Ask for the user's height in meters
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# Determine the BMI category
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 24.9:
    category = "normal weight"
elif 25 <= bmi < 29.9:
    category = "overweight"
else:
    category = "obese"

# Display the result
print(f"\n{name}, your BMI is: {bmi:.2f}. You are {category}.")
