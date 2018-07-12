def multiply(A, B):
    m = len(A)
    n = len(B)
    products = [[0]*(m+n) for _ in range(n)]
    
    for i in reversed(range(n)):
        carry = 0
        idx = m+i
        for j in reversed(range(m)):
            val = carry + A[j]*B[i]
            assert idx >= 0
            products[i][idx] = val%10
            carry = val/10
            idx -= 1
        products[i][idx] = carry
        # print(products[i])
        
    res = [0]*(m+n)
    carry = 0
    for i in reversed(range(n+m)):
        val = carry 
        for j in range(n):
            val += products[j][i]
        res[i] = val%10 
        carry = val/10
    while carry > 0:
        res = [carry%10] + res 
        carry /= 10
    # print res 
    
    return res 
    
def compare(A, target):
    square = multiply(A,A)
    # print square
    int_part = square[0]
    decimal_part = square[1:]
    
    if int_part < target-1:
        int_part = 10*int_part + square[1]
        decimal_part = square[2:]
        
    # print int_part
    if int_part < target:
        return -1 
    else:
        return 1
    
            
ans = 0
for target in range(2,100):
    approx = target**0.5 
    if abs(approx - round(approx)) < 1e-8:
        # perfect square 
        continue

    # print target
    root = map(int,list(str(approx).replace(".","")[:-1]))
    
    while len(root) < 100:
        root.append(0)
        low = 0
        high = 9
        while low < high:
            mid = (low+high+1)/2 
            root[-1] = mid 
            if compare(root, target) == 1:
                high = mid-1
            else:
                low = mid 
        root[-1] = low 
        
    ans += sum(root)
    # print root
    # break 

print ans 
