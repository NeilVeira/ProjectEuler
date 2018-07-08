MAXN = 1000000
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
tens = [10]
for _ in xrange(5):
    tens.append(10*tens[-1])
#print tens

def truncate(p):
    for t in tens:
        left = p % t
        #print left
        if not is_prime[left]:
            return False
        
    for t in tens:
        right = p/t
        #print right
        if right == 0:
            break
        elif not is_prime[right]:
            return False
    return True
        
is_prime[1] = False
ans = 0
cnt = 0
for p in primes:
    if p >= 10 and truncate(p):
        #print p
        ans += p
        cnt += 1
        
print cnt
print ans