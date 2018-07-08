def cancel(a,b):
    a = str(a)
    b = str(b)
    if a[1] == "0":
        return None,None
    if a[0] == b[0]:
        return int(a[1]),int(b[1])
    elif a[0] == b[1]:
        return int(a[1]),int(b[0])
    elif a[1] == b[0]:
        return int(a[0]),int(b[1])
    elif a[1] == b[1]:
        return int(a[0]),int(b[0])
    else:
        return None,None
    
def gcd(a,b):
    if a%b == 0:
        return b
    else: 
        return gcd(b,a%b)

num = 1
denom = 1
for a in xrange(10,100):
    for b in xrange(a+1,100):
        aa,bb = cancel(a,b)
        if aa != None and a*bb == aa*b:
            #print a,b,aa,bb
            num *= a
            denom *= b
            
g = gcd(num,denom)
print denom/g