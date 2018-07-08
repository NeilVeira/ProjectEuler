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
    return is_prime,primes


def is_prime_slow(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def check_prime(num):
    if num < len(is_prime):
        return is_prime[num]
    else:
        return is_prime_slow(num)


def concat(a,b):
    b_digits = []
    while b > 0:
        b_digits.append(b%10)
        b /= 10
    for d in reversed(b_digits):
        a = a*10 + d
    return a


def check(prev, p):
    for p2 in prev:
        num = concat(p2,p)
        if not check_prime(num):
            return False
        num = concat(p,p2)
        if not check_prime(num):
            return False
    return True
    

is_prime,primes = sieve(1000000)
n = 1229 #4-digit primes

for i in xrange(7):
    #print i
    
    for j in xrange(i+1,n):
        if not check([primes[i]],primes[j]):
            continue
        
        for k in xrange(j+1,n):
            if not check([primes[i],primes[j]], primes[k]):
                continue
            
            for l in xrange(k+1,n):
                if not check([primes[i],primes[j],primes[k]],primes[l]):
                    continue 
                
                for m in xrange(l+1,n):
                    if not check([primes[i],primes[j],primes[k],primes[l]], primes[m]):
                        continue
                    
                    #print primes[i],primes[j],primes[k],primes[l],primes[m]
                    print primes[i]+primes[j]+primes[k]+primes[l]+primes[m]


