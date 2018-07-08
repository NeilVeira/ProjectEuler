def divisor_sum(n):
    s = 1
    x = 2
    while x*x <= n:
        if n%x == 0:
            s += x
            if n/x != x:
                s += n/x
        x += 1
    return s

#print divisor_sum(220)
#print divisor_sum(284)

divisor_sums = [0,0]
for n in xrange(2,10000):
    divisor_sums.append(divisor_sum(n))
#print divisor_sums

ans = 0
for n in xrange(2,10000):
    if divisor_sums[n] >= 10000:
        if divisor_sum(divisor_sums[n]) == n:
            ans += n
    else:
        if divisor_sums[n] != n and divisor_sums[divisor_sums[n]] == n:
            #print n
            ans += n
print ans