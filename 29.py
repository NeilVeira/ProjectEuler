MOD = 10**9+7
vals = set([])
for a in xrange(2,101):
    for b in xrange(2,101):
        val = pow(a,b)
        vals.add(val)
        
#print vals
print len(vals)