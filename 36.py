def is_palindrome(s):
    return s[::-1] == s

def check(n):
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:])

ans = 0
for n in xrange(1,1000000):
    if check(n):
        ans += n
        #print n
print ans