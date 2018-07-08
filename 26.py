def long_divide(n):
    dividend = 1
    while dividend < n:
        dividend *= 10
    quotient = [0]
    history = []
    
    while dividend > 0 and dividend not in history:
        history.append(dividend)
        quotient.append(dividend/n)
        dividend %= n
        dividend *= 10
        
    if dividend != 0:
        history.reverse()
        return history.index(dividend)+1
    
ans = 0
best = 0
for n in xrange(2,1000):
    length = long_divide(n)
    if length and length > best:
        #print n,length
        best = length
        ans = n
print ans