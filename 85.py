best = 100000000  
ans = 0
for a in range(1,1000):
    for b in range(1,1000):
        ways = a*(a+1)*b*(b+1)/4
        if abs(ways-2000000) < best:
            best = abs(ways-2000000)
            ans = a*b 
print ans 
