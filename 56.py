def digit_sum(num):
    res = 0
    while num > 0:
        res += num%10
        num /= 10
    return res

ans = 0
for a in xrange(1,100):
    for b in xrange(1,100):
        num = a**b
        ans = max(ans, digit_sum(num))
print ans