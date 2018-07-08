def get_digits(num):
    digits = [0]*10
    while num > 0:
        digits[num%10] += 1
        num /= 10
    return digits

def check(num):
    target = get_digits(num)
    for f in xrange(2,7):
        mult = num*f
        digits = get_digits(mult)
        #print digits,target
        if digits != target:
            return False
    return True

length = 6
found = False
while not found:
    for num in xrange(10**(length-1), 10**length/6):
        #print num
        if check(num):
            print num
            found = True
            break
    length += 1
    