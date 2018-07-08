MAXN = 10000
is_prime = [True]*(MAXN+1)

def sieve(MAXN):
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

squares = []
i = 1
while i*i <= MAXN:
    squares.append(i*i)
    i += 1
    
conjecture = [False]*(MAXN+1)
for p in primes:
    for s in squares:
        num = p+2*s 
        if num <= MAXN:
            conjecture[num] = True 
#print conjecture

for i in xrange(3,MAXN+1):
    if i%2 == 1 and not is_prime[i] and not conjecture[i]:
        print i
        break