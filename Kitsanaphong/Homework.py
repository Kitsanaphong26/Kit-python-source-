def deposit(money):
   balance = 1000
   print(f"ยอดเงินเริ่มต้น: {balance} บาท")
   try:
       amount = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
       if amount <= 0:
           raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
   except ValueError as e:
       print(f"เกิดข้อผิดพลาด: {e}")
   else:
       balance += amount
       print("ฝากเงินสำเร็จ")
       print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
   finally:
       print("สิ้นสุดรายการฝากเงิน")

deposit(1000)