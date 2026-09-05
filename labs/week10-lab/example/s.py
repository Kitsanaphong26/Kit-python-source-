#เขียนโปรแกรม ตรวจสอบความแข็งแรงของ password
#password ที่แข็งแรงคือ ยาวมากกว่า 8 ตัว และผสมกันระหว่างตัวเลข ตัวอักษร และอักขระพิเศษ


password = input("Insert your password")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check ==False:
    print("Your password is strong!")
else:
    print("Your password is not strong!")