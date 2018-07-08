is_prime = [True]*(1000000+1)
def sieve(MAXN):
    for n in xrange(2,MAXN+1):
        if is_prime[n]:
            #for mult in xrange(2,MAXN/n+1):
            mult = 2
            while mult*n <= MAXN:
                is_prime[mult*n] = False
                mult += 1
    
    primes = []
    for n in xrange(2,MAXN+1):
        if is_prime[n]:
            primes.append(n)
    return primes

primes = sieve(1000000)
print len(primes)
maxlen = len(primes)
best_len = 0
ans = 0

for i in xrange(len(primes)):
    s = 0
    for l in xrange(maxlen):
        if i+l < len(primes):
            s += primes[i+l]
            if s > 1000000:
                break
            if l+1 > best_len and is_prime[s]:
                #print l+1,s
                best_len = l+1
                ans = s
                
print ans
