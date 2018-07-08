def lcm(a,b):
    return a*b/gcd(a,b)

def gcd(a,b):
    if a%b == 0:
        return b
    else: 
        return gcd(b,a%b)
    
ans = 1
for i in range(2,21):
    ans = lcm(ans,i)
print ans
