weight = float(input ("Weight(K.K.)"))
height = float(input("height(C.M."))
bmi =weight/(height **2)

if bmi < 18.5 :
    category = "Underweight"
elif bmi < 25.0 :
    category = "Normal weight"
elif bmi < 30.0 :
    category = "Dverweight"
else :
    category = "Obese"

print (f"BMI : {bmi}")
print (f"{category}")