def is_pandigital(*nums):
    used = [False]*10
    for num in nums:
        s = str(num)
        if "0" in s:
            return False
        
        for c in s:
            if used[int(c)]:
                return False
            used[int(c)] = True
    return True

products = set([])
for a in xrange(1,10**5):
    if is_pandigital(a):
        alen = len(str(a))
        for b in xrange(1,10**5):
            blen = len(str(b))
            prod = a*b
            if len(str(prod)) + alen + blen > 9:
                break
            if is_pandigital(a,b,prod) and len(str(prod))+alen+blen == 9:
                print a,b,prod
                products.add(prod)
                
ans = 0
for p in products:
    ans += p
print ans