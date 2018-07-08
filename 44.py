import math

def is_pent(x):
    det = 1 + 24*x
    det_root = int(math.sqrt(det))
    if (det_root+1)**2 == det:
        det_root += 1
    
    n = (1 + det_root)/6
    
    return n*(3*n-1)/2 == x

pents = []
for n in xrange(1,10000):
    pents.append(n*(3*n-1)/2)

found = False
for i in xrange(len(pents)):
    D = pents[i]
    
    for j in xrange(i+1,len(pents)):
        S = pents[j]
        if (D+S)%2 == 0:
            p1 = (D+S)/2
            p2 = (S-D)/2
            if is_pent(p1) and is_pent(p2):
                print D
                found = True
                break
            
    if found:
        break