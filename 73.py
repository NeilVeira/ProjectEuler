ans = 0 
MAXN = 12000

s = [(1,2,1,3)]
while len(s) > 0:
    a,b,c,d = s[-1]
    if b+d <= MAXN:
        ans += 1
        s[-1] = (a,b,a+c,b+d)
        s.append((a+c,b+d,c,d))
    else:
        del s[-1]
        
print ans 