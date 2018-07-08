pents = []
for k in range(1,1000):
    pents.append(k*(3*k-1)/2)
    pents.append(-k*(3*(-k)-1)/2)

p = [1]
n = 1
while True:
    sign = 0
    cur = 0
    for i in pents:
        if i > n:
            break
        if sign < 2:
            cur += p[n-i]
        else:
            cur -= p[n-i]
        sign = (sign+1)%4 
        
    cur %= 1000000
    if cur == 0:
        print n
        break
    p.append(cur)
    n += 1
