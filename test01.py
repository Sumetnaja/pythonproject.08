#-------Set คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันไม่ได้ (ถ้าซ้ำถือว่าเป็นตัวเดียว) และไม่มีลำดับ และแก้ไขไม่ได้ แต่เพิ่ม ลดได้--------
my_set1 = {10, 20, True, 10, 'SAU', (20, 'IOT')}

#ไม่สามารถที่จะเข้าถึงข้อมูลใดข้อมูลหนึ่งได้
#เข้าถึงทุกข้อมูลใน Set
for data in my_set1 :
    print(data)

# แก้ไขข้อมูลใน Set ทำไม่ได้โดยตรง แต่ทำได้โดยอ้อมเหมือนกับ Tuple
my_list = list( my_set1 )
print(my_list)
my_list[2] = 'IOT'
print(my_list)
my_set1 = set(my_list)
print(my_set1)

# Set Method
my_set1.add(999)
my_set1.add('Wow')
print(my_set1)
my_set1.pop()
print(my_set1)
my_set2 = my_set1.copy()
print(my_set2)
my_set1.remove(999)
print(my_set1)

# Set Function
# len()
print( len(my_set1) )
# min(), max()
my_set3 = {10, 30, 20, 5, 999}
print( min(my_set3) )
print( max(my_set3) )