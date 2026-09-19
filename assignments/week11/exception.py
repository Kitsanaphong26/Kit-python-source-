"""
โจทย์ 1 : เครื่องคำนวณอย่างปลอดภัย
เขียนโปรแกรมรับตัวเลข 2 จำนวนและดำเนินการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์
โปรแกรมต้องจัดการกรณีต่อไปนี้
ฺ* ผู้ใช้กรอกข้อมูลที่ไม่ใช้ตัวเลข #ValueError
* ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก + - * / raise ValueError
* ผู้ใช้พยายามหารตัวเลขด้วยศูนย์ #ZeroDivisionError
* โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย Finally
 
ตัวอย่างการแสดงผล
ตัวเลขที่ 1 : 10
ตัวเลขที่ 2 : 0
เครื่องหมาย (+ - * /) : /
 
ไม่สามารถหารด้วยศูนย์ได้
จบการทำงาน
"""
 
#mycode
 
try:
    num1 = float(input("ตัวเลขที่ 1 : "))
    num2 = float(input("ตัวเลขที่ 2 : "))
    operator = input("เครื่องหมาย (+ , - , * , /) : ")
    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น ( + - * / ) เท่านั้น")
    print(f"{num1} {operator} {num2} = {result}")
except ValueError: #กรณีผู้ใช้ไม่พิมพ์ตัวเลข
    print("กรอกอายุเป็นตัวเลขจำนวนเต็ม เช่น 20")
except ZeroDivisionError: #กรณีผู้ใช้ใส่ num2 เป็น 0
    print("ไม่สามารถหารด้วยศูนย์ได้")
#except Exception: #กรณีอื่นๆ
    print("")
else:#จะทำที่นี่ก็ต่อเมื่อไม่มี Exception
    print("คำนวณข้อมูลเรียบร้อยแล้ว")
 
finally:#ทำเสมอไม่ว่าจะมีหรือไม่มี Exception
    print("จบการทำงาน")