def reverse(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num%10
        num /= 10
    return rev

def is_palindrome(num):
    return reverse(num) == num

def is_lychrel(num):
    for iters in xrange(50):
        num += reverse(num)
        #print num
        if is_palindrome(num):
            return False
    return True

ans = 0
for i in xrange(10000):
    if is_lychrel(i):
        ans += 1
        #print i
print ans