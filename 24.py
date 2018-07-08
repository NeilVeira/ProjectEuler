from math import factorial as fact

def nth_permutation(n,r):
    n -= 1
    digits = range(r)
    perm = []
    
    while r > 0:
        f = fact(r-1)
        idx = n/f
        #print n,f,idx
        perm.append(digits[idx])
        del digits[idx]
        n %= f
        r -= 1
    return perm
        
perm = nth_permutation(1000000,10)
print perm
print "".join(map(str,perm))
