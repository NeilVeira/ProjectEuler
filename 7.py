def is_prime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

cnt = 0
p = 1
while cnt < 10001:
    p += 1
    if is_prime(p):
        cnt += 1

print p