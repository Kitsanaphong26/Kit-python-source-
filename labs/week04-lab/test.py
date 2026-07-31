#รับข้อมูล ชื่อจริง เป็นภาษาอังกฤษ จากผู้ใช้
#นับจำนวนสระในข้อความดังกล่าว
 
#ตัวอย่าง
#What is your name? : Kitsanaphong
# You have 4 vowels in your text.
 
 
#name = input ("What is your name ? : ")
name = "Kitsanaphong"
letters = list(name)
print(letters)
counter = 0
 
#ท่าที่1
for char in letters:
    if char == 'a' or  char == 'A':
        counter = counter +1
 
    if char == 'e' or  char == 'E':
        counter = counter +1
       
    if char == 'i' or  char == 'I':
        counter = counter +1
 
    if char == 'o' or  char == 'O':
        counter = counter +1
 
    if char == 'u' or  char == 'U':
        counter = counter +1
 
print( "You have",counter,"vowels in your tex")
 
#ท่าที่ 2
a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')
A = letters.count('A')
E = letters.count('E')
I = letters.count('I')
O = letters.count('O')
U = letters.count('U')
 
vowels = a + e + i + o + u + A + E + I + O + U
print("You have", counter,"vowels in your tex")
print(f"You have, (vowels) vowels in your tex")