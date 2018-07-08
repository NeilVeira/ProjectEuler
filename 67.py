f = open("67.txt")
triangle = []
for line in f:
    triangle.append(map(int,line.split()))
    
h = len(triangle)
w = len(triangle[-1])
dp = [[None]*w for _ in range(h)]
for i in xrange(w):
    dp[h-1][i] = triangle[h-1][i]

    
for y in reversed(range(h-1)):
    for x in xrange(y+1):
        dp[y][x] = triangle[y][x] + max(dp[y+1][x],dp[y+1][x+1])
#for row in dp:
#    print row
    
print dp[0][0]