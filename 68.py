def get_digit_string(digits):
    string = ""
    start = -1
    for i in xrange(5,10):
        if start == -1 or digits[i] < digits[start]:
            start = i
          
    cur = start
    for i in xrange(5):
        string += str(digits[cur])
        string += str(digits[cur-5])
        string += str(digits[(cur-5+1)%5])
        cur += 1
        if cur == 10:
            cur = 5
    return string

def find_outer(used,digits,s):
    for i in xrange(5,10):
        cur_sum = digits[i-5]+digits[(i-5+1)%5]
        d = s-cur_sum
        if d <= 0 or d > 10 or used[d]:
            return False
        used[d] = True
        digits[i] = d
    
    digit_string = get_digit_string(digits)
    global max_digit_string
    if len(digit_string) == 16 and int(digit_string) > int(max_digit_string):
        max_digit_string = digit_string
    return True
        

def place_ring(i):
    if i == 5:
        for s in xrange(30):
            find_outer(list(used),list(digits),s)
    else:
        for d in xrange(1,11):
            if not used[d]:
                digits[i] = d
                used[d] = True
                place_ring(i+1)
                used[d] = False

max_digit_string = "0"
used = [False]*11
digits = [0]*10

#print get_digit_string([1,2,3,4,5,6,7,8,9,10])
place_ring(0)
print max_digit_string