#lets learn how to take input


person_A_name = input ("What is your name:")
person_A_age = input ("Enter your age in years:")
person_B_name = input ("What is your name:")
person_B_age = input("Enter your age in years:")
if person_A_age > person_B_age:
    print(person_A_name, "is older than", person_B_name)
else:
    print(person_A_name, "is younger than", person_B_name)