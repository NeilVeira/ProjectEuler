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

def prime_factorize(n, primes):
    factors = []
    for p in primes:
        if n%p == 0:
            factors.append(p)
        while n%p == 0:
            n /= p
        if n < p:
            break
    if n != 1:
        factors.append(n)
    return factors

'''
def check_distinct(primes1, primes2):
    for p in primes1:
        if p in primes2:
            return False
    return True

def check_multidistinct(all_factors):
    seen = []
    for factor_set in all_factors:
        if not check_distinct(seen, factor_set):
            seen.extend(factor_set)
            return False 
    return True
'''

MAXN = 1000
M = 4
all_factors = [[]]*M
primes = sieve(MAXN)
seq = 0
for n in xrange(2,MAXN*MAXN):
    factors = prime_factorize(n, primes)
    if len(factors) == M:
        seq += 1
        if seq == M:
            print n-M+1
            break
    else:
        seq = 0
    
    