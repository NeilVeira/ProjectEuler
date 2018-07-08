import math 
import numpy as np

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
    return primes


def get_digit_cnt(n):
    cnt = np.zeros((10), dtype=np.int32)
    while n > 0:
        cnt[n%10] += 1
        n /= 10
    return cnt

def is_perm(a,b):
    cnt1 = get_digit_cnt(a)
    cnt2 = get_digit_cnt(b)
    return all(cnt1 == cnt2)


MAXN = 10000000
phi_by_n = [1]*(MAXN+1)
is_prime = [True]*(MAXN+1)

for i in xrange(2,MAXN):
    if is_prime[i]:
        for m in xrange(1,MAXN/i+1):
            phi_by_n[i*m] *= 1-1.0/i
            is_prime[i*m] = False

best = 0
ans = 0
for i in xrange(MAXN/10,MAXN):
    phi = int(round(i*phi_by_n[i]))
    if phi >= MAXN/10:
        if is_perm(i,phi) and phi_by_n[i] > best:
            best = phi_by_n[i]
            ans = i
print ans
