weight = int(input("What is your weight?\n>> "))
height = int(input("What is your height?\n>> "))

bmi = weight / (height ** 2)

round_bmi = round(bmi * 10000,2)
print(""
      "Underweight:        BMI <= 18.5\n"
      "Normal:      18.5 > BMI < 25\n"
      "Overweight:         BMI > 25\n")

if round_bmi < 18.5:
    print(f"Your BMI is: {round_bmi}, that means you are underweight.")
elif round_bmi >= 18.5 and round_bmi < 25:
    print(f"Your BMI is: {round_bmi}, that means your weight is normal.")
else:
    print(f"Your BMI is: {round_bmi}, that means you are overweight.")
lose = 
put_up =
print(f"In order to be normal weight you should lose {lose} kilos")
print(f"In order to be normal weight you should put up {put_up} kilos")