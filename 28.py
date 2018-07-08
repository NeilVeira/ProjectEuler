N = 1001
DX = [1,0,-1,0]
DY = [0,1,0,-1]

def print_spiral(spiral):
    for row in spiral:
        for num in row:
            print str(num).rjust(4),
        print ""
    print ""

spiral = [[0]*N for _ in range(N)]
num = 1
x = N/2
y = N/2
direc = 0
distances = []
for i in xrange(N):
    distances.append(i+1)
    distances.append(i+1)
dist_idx = 0

while 0 <= x < N and 0 <= y < N:
    dist = distances[dist_idx]
    #print dist
    for _ in xrange(dist):
        #print x,y,num
        spiral[y][x] = num
        x += DX[direc]
        y += DY[direc]
        num += 1
    direc = (direc+1)%4
    dist_idx += 1
    
#print_spiral(spiral)
    
ans = 0
for i in xrange(N):
    ans += spiral[i][i]
    ans += spiral[i][N-i-1]
ans -= spiral[N/2][N/2]
print ans