import math

while True:
    try:
        n = (int(input("Nhập số nguyên n: ")))
        break
    except ValueError:
        print("Lỗi: Bạn phải nhập đúng số nguyên!")

# Hiển thị n ở dạng nhị phân
print("Dạng nhị phân của n:", '1' + str(bin(n)[3:]).zfill(16) if n < 0 else bin(n)[2:])
    
# Hàm tính tổng các chữ số
def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))

# Nhập lại n mà ko ktra và tính tổng
n2 = int(input('Nhập lại n: '))
print("Tổng các chữ số của n:", sum_of_digits(n2))

# Hàm đảo ngược
def reverse_number(num):
    if num < 0:
        return -int(str(abs(num))[::-1])
    return int(str(num)[::-1])

# Đảo ngược số n
m = reverse_number(n2)
print("Số đảo ngược m:", m)