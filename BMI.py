# Welcome to the BIM calculator APP
# The app will ask you about your height and weight
height = float(input("what is your height in metters: "))
weight = float(input("what is your weight in kg: "))

# The calculation is : BMI = weight / height ** 2
BMI_result = round(weight / height ** 2, 2)

# The app conditions
if BMI_result < 18.5: # Under 18.5 they are underweight
    print(f"your BMI is {BMI_result}, you are underweight")
elif BMI_result < 25: # Over 18.5 but below 25 they have a normal weight
    print(f"your BMI is {BMI_result}, you have a normal weight")
elif BMI_result < 30: # Over 25 but below 30 they are overweight
    print(f"your BMI is {BMI_result}, you are overweight")
elif BMI_result < 35: # Over 30 but below 35 they are obese
    print(f"your BMI is {BMI_result}, you are obese")
else: # Above 35 they are clinically obese
    print(f"your BMI is {BMI_result}, you are clinically obese")    

































