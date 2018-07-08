MAXN = 1000000
phi_by_n = [1]*(MAXN+1)
is_prime = [True]*(MAXN+1)

for i in xrange(2,MAXN+1):
    if is_prime[i]:
        for m in xrange(1,MAXN/i+1):
            phi_by_n[i*m] *= 1-1.0/i
            is_prime[i*m] = False
            
ans = 0
for i in range(2,MAXN+1):
    phi = int(round(phi_by_n[i]*i))
    #print i,phi
    ans += phi
print ans
    