f = open("82.txt")
grid = []
for line in f:
    grid.append(map(int,line.split(",")))
n = len(grid)

dp = [[1e20]*(n+1) for _ in range(n)]
for i in range(n):
    dp[i][n] = 0 

for j in reversed(range(n)):
    for i in range(n):
        s = 0
        for k in reversed(range(i+1)):
            s += grid[k][j]
            dp[i][j] = min(dp[i][j], s+dp[k][j+1])
        s = 0 
        for k in range(i,n):
            s += grid[k][j]
            dp[i][j] = min(dp[i][j], s+dp[k][j+1])
            
ans = min(dp[i][0] for i in range(n))
print ans 
