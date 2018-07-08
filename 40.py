def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n /= 10
    digits.reverse()
    return digits

digits = []
ans = 1
num = 1
while len(digits) < 1000000:
    digits.extend(get_digits(num))
    num += 1
#print digits

for idx in [1,10,100,1000,10000,100000,1000000]:
    ans *= digits[idx-1]
print ans