num,den = 3,2
ans = 0
for i in xrange(2,1001):
    num += den
    num,den = den,num
    num += den
    #print num,den
    if len(str(num)) > len(str(den)):
        ans += 1
print ans