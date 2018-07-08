def test(n):
    seen_digits = [False]*10
    seen_digits[0] = True
    pan_num = 0
    
    for mult in xrange(1,10):
        if False not in seen_digits:
            return pan_num
        prod = n*mult
        #print prod
        tmp = []
        while prod > 0:
            digit = prod%10
            if seen_digits[digit]:
                return None
            seen_digits[digit] = True
            tmp.append(digit)
            prod /= 10
            
        for digit in reversed(tmp):
            pan_num = 10*pan_num + digit
        
ans = 0
for i in xrange(1,10000):
    result = test(i)
    if result != None:
        #print i,result
        ans = max(ans,result)
print ans