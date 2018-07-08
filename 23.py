def is_abundant(n):
    s = 1
    x = 2
    while x*x <= n:
        if n%x == 0:
            s += x
            if n/x != x:
                s += n/x
        x += 1
    return s > n

abundants = []
for i in xrange(2,28123):
    if is_abundant(i):
        abundants.append(i)
print len(abundants)

can_sum = [False]*28123
for a in abundants:
    for b in abundants:
        if a + b >= 28123:
            break
        can_sum[a+b] = True

ans = 0
for i in xrange(1,28123):
    if not can_sum[i]:
        ans += i
        #print i
print ans