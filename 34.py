fact = [1]
for i in xrange(1,10):
    fact.append(fact[-1]*i)

def check(a):
    s = 0
    for digit in str(a):
        s += fact[int(digit)]
    return s == a

ans = 0
for i in xrange(10,100000):
    if check(i):
        ans += i
        #print i
print ans