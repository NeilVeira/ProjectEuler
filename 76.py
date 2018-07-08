MAXN = 100
ways = [0]*(MAXN+1)
ways[0] = 1

for i in range(1,MAXN+1):
    for j in range(i,MAXN+1):
        ways[j] += ways[j-i]
print ways[MAXN]-1
