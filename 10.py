def sieve(MAXN):
    is_prime = [True]*(MAXN+1)
    for n in xrange(2,MAXN+1):
        if is_prime[n]:
            for mult in xrange(2,MAXN/n+1):
                is_prime[mult*n] = False
    
    primes = []
    for n in xrange(2,MAXN+1):
        if is_prime[n]:
            primes.append(n)
    return primes

primes = sieve(2000000)
#print primes
print sum(primes)