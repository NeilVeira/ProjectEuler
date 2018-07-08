import math

sols = [0]*1001
for a in xrange(1,334):
    for b in xrange(a+1,1000-a+1):
        c = int(math.sqrt(a**2+b**2))
        if a**2 + b**2 == c**2:
            p = a+b+c
            #print a,b,c,p
            if p <= 1000:
                sols[p] += 1
        elif a**2 + b**2 == (c+1)**2:
            p = a+b+c+1
            #print a,b,c+1,p
            if p <= 1000:
                sols[p] += 1
        
#print sols
m = max(sols)
#print m
for p in xrange(1,1001):
    if sols[p] == m:
        print p
        break