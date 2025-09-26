import math

while True:
    try:
        n = int(input("Nhập số nguyên n (n > 5): "))
        if n > 5:
            break
        else:
            print("n phải lớn hơn 5. Hãy nhập lại!")
    except ValueError:
        print("Lỗi: Bạn phải nhập số nguyên!")

S1 = sum(range(1, n + 1))

S2 = math.factorial(n)

S3 = f'{sum(1 / i for i in range(1, n + 1)):.2f}'

print(f"S1 = {S1}")
print(f"S2 = {S2}")
print(f"S3 = {S3}")

# Hàm kiểm tra số nguyên tố
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Nhập lại số n
while True:
    try:
        n2 = int(input("Nhập lại số nguyên để kiểm tra số nguyên tố: "))
        break
    except ValueError:
        print("Lỗi: Bạn phải nhập số nguyên!")

# Kiểm tra xem số nguyên tố
if is_prime(n2):
    print(f"'{n2}' là số nguyên tố.")
else:
    print(f"'{n2}' không phải số nguyên tố.")