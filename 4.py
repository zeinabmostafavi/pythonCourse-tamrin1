height = float(input("please Enter your height(m)"))
weight = float(input("please Enter your weight(kg)"))

BMI = float(weight / (height ** 2))
if BMI < 18.5:
    print("under weight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal")
elif BMI >= 25 and BMI <= 29.9:
    print("overweight")
elif BMI >= 30 and BMI <= 34.9:
    print("obese")
elif BMI >= 35:
    print("Externely obese")