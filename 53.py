C = [[0]*101 for r in xrange(101)]
for n in xrange(1,101):
    C[n][0] = C[n][n] = 1
    for r in xrange(1,n):
        C[n][r] = C[n-1][r] + C[n-1][r-1]
#for row in C:
#    print row
    
ans = 0
for n in xrange(101):
    for r in xrange(101):
        if C[n][r] > 1000000:
            ans += 1
print ans