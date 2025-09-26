import math

while True:
    try:
        m, n = map(int, input("Nhập 2 số nguyên m và n: ").split())
        if m > 0 and n > 0:
            break
        else: print(' 2 số phải dương')
    except ValueError:
        print("Lỗi: Bạn phải nhập đúng 2 số nguyên!")

# Hàm tìm ước nguyên tố
def prime_factors(num):
    factors = set()
    i = 2
    while i * i <= num:
        while num % i == 0:
            factors.add(i)
            num //= i
        i += 1
    if num > 1:
        factors.add(num)
    return factors

# 1. Tìm ước số nguyên tố chung
common_primes = prime_factors(m).intersection(prime_factors(n))
print("Các ước số nguyên tố chung:", common_primes if common_primes else "Không có")

# 2. GCD
gcd_val = math.gcd(m, n)
print("Ước số chung lớn nhất (GCD):", gcd_val)

# 3. LCM
lcm_val = abs(m * n) // gcd_val if gcd_val != 0 else 0
print("Bội số chung nhỏ nhất (LCM):", lcm_val)