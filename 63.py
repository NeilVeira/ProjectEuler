ans = 1 #1^1 has 1 digit

for base in xrange(2,10):
    for n in xrange(1,100):
        l = len(str(base**n))
        if l == n:
            ans += 1
        #print n,l,n/float(l)
print ans