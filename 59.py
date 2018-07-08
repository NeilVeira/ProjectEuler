ALLOWED_CHARS = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm ,.!()-';:1234567890"

def decrypt(msg, key):
    ans = 0
    for i in xrange(len(msg)):
        m = msg[i] ^ key[i%len(key)]
        if chr(m) not in ALLOWED_CHARS:
            return -1 
        else:
            ans += m
    return ans
        

msg = map(int,open("59.txt").read().split(","))
key = []
for i in xrange(ord("a"),ord("z")+1):
    for j in xrange(ord("a"),ord("z")+1):
        for k in xrange(ord("a"),ord("z")+1):
            res = decrypt(msg, [i,j,k])
            if res != -1:
                print res
                break