import itertools

def is_prime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

ans = 0
for length in xrange(1,10):
    for digits in itertools.permutations(range(1,length+1)):
        n = 0
        for i in xrange(length):
            n = n*10 + digits[i]
        #print n
        if is_prime(n):
            ans = max(ans,n)
print ans