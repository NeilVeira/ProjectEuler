import itertools

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


def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n /= 10
    #digits.reverse()
    return digits


def valid_digits(digits):
    copy = list(digits)
    copy.sort()
    if digits != copy:
        return False
    return True


def find_prime_arith_seq(perms):
    results = []
    for i in xrange(len(perms)-2):
        if not is_prime[perms[i]]:
            continue
        for j in xrange(i+1,len(perms)-1):
            if not is_prime[perms[j]]:
                continue
            step = perms[j]-perms[i]
            other = perms[j] + step
            if other in perms and is_prime[other]:
                results.append((perms[i], perms[j], other))
    return results
            

def check_digits(digits):
    perms = []
    for perm in itertools.permutations(digits):
        num = 0
        for i in xrange(len(perm)):
            num += 10**i * perm[i]
        #print num
        if num >= 1000 and num not in perms:
            perms.append(num)
        
    perms.sort()
    #print perms
    return find_prime_arith_seq(perms)
    


sieve(10000)
for num in xrange(1000,10000):
    digits = get_digits(num)
    if valid_digits(digits):
        #print digits
        res = check_digits(digits)
        if len(res) > 0:
            print res

#res = check_digits([1,4,7,8])
#print res

