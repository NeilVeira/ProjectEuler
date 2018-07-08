def is_prime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def is_circular(n):
    s = str(n)
    for d in "02468":
        if d in s:
            return False
        
    for _ in xrange(len(s)):
        num = int(s)
        if not is_prime(num):
            return False
        s = s[1:]+s[0]
    return True

ans = 1
for n in xrange(3,1000000):
    if is_circular(n):
        #print n
        ans += 1
print ans