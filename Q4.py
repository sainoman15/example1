import math

while True:
    try:
        m, n = map(int, input("Nhập 2 số nguyên m và n: ").split())
        if m < n:
            break
        else:
            print("m phải nhỏ hơn n!")
    except ValueError:
        print("Lỗi: Bạn phải nhập đúng 2 số nguyên!")

# Hàm ktra xem đối xứng hay ko
def is_palindrome(num):
     return str(num) == str(num)[::-1]

# In ra số đối xứng
print(f'Các số đối xứng trong khoảng [{m} , {n}]: ')
found = False
for i in range(m, n+1):
    if is_palindrome(i):
            print(i, end=' ')
            found = True
if not found:
     print('Không có số đối xứng nào')