def is_prime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


prime_cnt = 0
total_cnt = 0
num = 1
dif = 2
while num < 10 or float(prime_cnt)/total_cnt >= 0.10:
    for _ in xrange(4):
        num += dif
        total_cnt += 1
        if is_prime(num):
            prime_cnt += 1
    dif += 2
    
print dif-3
    