import itertools

def get_digits(num):
    digits = []
    while num > 0:
        digits.append(num%10)
        num /= 10
    digits.reverse()
    return digits

def generate_nums(f):
    nums = {}
    n = 1
    while True:
        x = f(n)
        if x >= 10000:
            break
        elif x >= 1000:
            key = x/100
            if not nums.has_key(key):
                nums[key] = []
            nums[key].append(x)
        n += 1
    return nums 


def solve(all_nums, i, key, first_val):
    if not all_nums[i].has_key(key):
        return -1
    
    if i == 5:
        for num in all_nums[i][key]:
            if num%100 == first_val:
                return num
    else:
        for num in all_nums[i][key]:
            res = solve(all_nums, i+1, num%100, first_val)
            if res != -1:
                return res + num
    return -1

nums1 = generate_nums(lambda n: n*(n+1)/2)
nums2 = generate_nums(lambda n: n*n)
nums3 = generate_nums(lambda n: n*(3*n-1)/2)
nums4 = generate_nums(lambda n: n*(2*n-1))
nums5 = generate_nums(lambda n: n*(5*n-3)/2)
nums6 = generate_nums(lambda n: n*(3*n-2))

ans = -1
for perm in itertools.permutations([nums2,nums3,nums4,nums5,nums6]):
    all_nums = [nums1] + list(perm)
    for key in nums1:
        for num in nums1[key]:
            res = solve(all_nums, 1, num%100, key)
            if res != -1:
                ans = res+num
                break
        if ans != -1:
            break
    if ans != -1:
        break
        
print ans    
