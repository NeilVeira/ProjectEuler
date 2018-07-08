adj = [[False]*10 for _ in range(10)]
digits = set([])
for line in open("79.txt"):
    for i in range(2):
        a = int(line[i])
        b = int(line[i+1])
        adj[a][b] = True 
        digits.add(a)
        digits.add(b)

indegrees = [0]*10
for i in range(10):
    for j in range(10):
        indegrees[j] += int(adj[i][j])
        
order = []
while True:
    for i in digits:
        if indegrees[i] == 0:
            order.append(i)
            for j in digits:
                if adj[i][j]:
                    indegrees[j] -= 1
            indegrees[i] = -1 # done 
            break 
    else:
        break

print "".join(map(str,order))