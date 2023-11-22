height = float(input("Whats your height"))

weight = int(input("Whast your weight"))
bmi = weight / (height * height)

if bmi < 18.5:
    print(f"your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"your BMI is {bmi},you have normal weight")
elif bmi < 30:
    print(f"your BMI is{bmi}, you are over")
else:
    print("Bye")

