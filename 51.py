def is_prime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

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

def validity_check(digits, subset):
    val = None
    for i in xrange(len(digits)):
        if subset & 1<<i:
            if val == None:
                val = digits[i]
            if digits[i] != val:
                return False
    return True
            

def replace_digits(digits, subset):
    prime_cnt = 0
    length = len(digits)
    
    for new_digit in xrange(10):
        num = 0
        for i in xrange(length):
            if subset & (1<<i):
                num = 10*num + new_digit
            else:
                num = 10*num + digits[i]
        if num >= 10**(length-1) and is_prime[num]:
            #print num
            prime_cnt += 1
    return prime_cnt
        

primes = sieve(MAXN)

found = False
for p in primes:
    digits = []
    tmp = p
    while tmp > 0:
        digits.append(tmp%10)
        tmp /= 10
    digits.reverse()
    num_digits = len(digits)
    
    for subset in xrange(1,1<<num_digits):
        if validity_check(digits, subset):
            prime_cnt = replace_digits(digits, subset)
            if prime_cnt >= 8:
                print p
                found = True
                break
        
    if found:
        break

