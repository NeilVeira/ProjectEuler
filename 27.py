is_prime = [True]*(100001)

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


def prime_cbeck(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def check_formula(a,b):
    cnt = 0
    n = 0
    while True:
        val = n*n + a*n + b
        if val <= 0:
            break
        elif val >= len(is_prime):
            if not check_prime(val):
                break
        elif not is_prime[val]:
            break
        else:
            cnt += 1
        n += 1
    return cnt

primes = sieve(100000)


ans = 0
best = 0
for b in primes:
    if b >= 1000:
        break
    for a in xrange(-999,1000):
        cnt = check_formula(a,b)
        if cnt > best:
            #print a,b,cnt
            best = cnt
            ans = a*b
print ans