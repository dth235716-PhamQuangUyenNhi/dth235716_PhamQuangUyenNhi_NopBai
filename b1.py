from os import name
import sys
import math

print("Ví dụ 1: chương trình cộng 2 số")
#nhap so
so1 = int(input("Nhap so  thu nhat: "))
so2 = int(input("Nhap so  thu hai: "))

#tinh tong
tong = so1 + so2

#hien thi ket qua
print("Tong cua hai la: ", tong)



print("Ví dụ 2: cú pháp Python cơ bản")
#khai báo biến
x = 5

#in giá trị biến  
print("Giá trị của x là:", x)

#lệnh if_else
if x > 10:
    print("x lớn hơn 10")
else:
    print("x không lớn hơn 10")

#vòng lặp for
for i in range(5):
    print(i)

#nhập chuỗi
def hello(name):
    print ("Xin chao,", {name})



print("Ví dụ 3: câu lệnh, khối lệnh, chú thích")
#câu lệnh
a = 10  # gán giá trị 10 cho biến a đây là môt chú thích

#khối lệnh
if a > 10:
    print("a lớn hơn 10")
    print("Đây là khối lệnh")


print("Ví dụ 4: Nhập xuất dữ liệu từ bàn phím")
#nhập dữ liệu từ bàn phím
name = input("Nhập tên của bạn: ")
print("Xin chào,", name)

age = int(input("Nhập tuổi của bạn: "))
print("Tuổi của bạn là: ", age, "tuổi")

#Xuất dữ liệu'
name = "John"
age = 25
height = 1.75

print("Tên: ",name)
print("Tuổi: ",age)
print("Chiều cao: ",height)


print("Ví dụ 5: Mô đun")
number = 16
square_root = math.sqrt(number)

print("Căn bậc hai của", number, "là", square_root)