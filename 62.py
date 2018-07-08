actual_cubex = {}
cnt = {}
for i in xrange(1,10000):
    cube = i**3
    digits = list(str(cube))
    digits.sort()
    digits = "".join(digits)
    if not cnt.has_key(digits):
        cnt[digits] = 0
        actual_cubex[digits] = cube
    cnt[digits] += 1
    actual_cubex[digits] = min(actual_cubex[digits],cube)
    
#print cnt
ans = 999999999999999999999999
for item in cnt:
    if cnt[item] >= 5:
        #print item,actual_cubex[item]
        ans = min(ans,actual_cubex[item])
print ans