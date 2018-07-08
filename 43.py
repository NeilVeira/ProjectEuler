divisor_checks = [1,1,1,2,3,5,7,11,13,17]

ans = 0

def solve(i, cur_num, used_digit):
    if i == 10:
        #print cur_num
        global ans
        ans += cur_num
    else:
        for d in xrange(10):
            if not used_digit[d]:
                next_num = cur_num*10 + d
                if (next_num%1000) % divisor_checks[i] == 0:
                    used_digit[d] = True
                    solve(i+1, next_num, used_digit)
                    used_digit[d] = False
    
solve(0, 0, [False]*10)
print ans