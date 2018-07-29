f = open("81.txt")
grid = []
for line in f:
    grid.append(map(int,line.split(",")))
n = len(grid)

best = [[1e20]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        prev = 0
        if i > 0:
            if j > 0:
                prev = min(best[i-1][j], best[i][j-1])
            else:
                prev = best[i-1][j]
        else:
            if j > 0:
                prev = best[i][j-1]
            else:
                prev = 0
        best[i][j] = prev + grid[i][j]
        
print best[n-1][n-1]