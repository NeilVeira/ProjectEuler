MAXN = 100

def sieve(MAXN):
    '''
    Sieve of Eratosthenes up to MAXN (inclusive)
    '''
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
    
primes = sieve(MAXN)
ways = [0]*(MAXN+1)
ways[0] = 1
for p in primes:
    for i in range(p,MAXN+1):
        ways[i] += ways[i-p]

for i in range(MAXN+1):
    if ways[i] > 5000:
        print i 
        break 
