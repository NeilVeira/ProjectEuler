def gcd(a,b):
    '''
    Greatest common divisor
    '''
    if a%b == 0:
        return b
    else: 
        return gcd(b,a%b)

def compare(f1,f2):
    #return true if fraction f1 > f2
    return f1[0]*f2[1] > f1[1]*f2[0] 

best = (0,1)
for d in range(8,1000001):    
    n = 3*d/7
    while gcd(n,d) > 1:
        n -= 1
    if compare((n,d), best):
        best = (n,d)
print best[0]