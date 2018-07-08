MAXN = 1000000
lengths = [None]*(3*MAXN+1)
lengths[0] = 0
lengths[1] = 1

def do(x):
    #if x >= len(lengths):
    #    lengths.extend([None]*(x-len(lengths)+1))
    if x < len(lengths) and lengths[x] != None:
        return lengths[x]
    elif x&1 == 1:
        res = do(3*x+1)+1
    else:
        res = do(x/2)+1
    if x < len(lengths):
        lengths[x] = res
    return res

ans = 0
longest = 0
for start in xrange(2,MAXN):
    if lengths[start] == None:
        if start%1000 == 0:
            print start
        res = do(start)
        if res > longest:
            longest = res
            ans = start
#print len(lengths)
#print lengths
print ans,longest