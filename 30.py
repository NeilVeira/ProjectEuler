def pow_digits(n):
    ans = 0
    while n > 0:
        digit = n%10
        ans += digit**5
        n /= 10
    return ans

Max = 5*9**5
ans = 0
for i in xrange(10,Max):
    if pow_digits(i) == i:
        #print i
        ans += i
print ans