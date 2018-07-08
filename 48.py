MOD = 10**10
ans = 0
for x in xrange(1,1001):
    ans += pow(x,x,MOD)
print ans%MOD