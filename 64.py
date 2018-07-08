import math

class Num(object):
    def __init__(self, root, a=0, b=1):
        self.root = root
        self.a = a
        self.b = b
        
    def get_val(self):
        return (math.sqrt(self.root)+self.a) / self.b
    
    def get_int(self):
        return int(self.get_val())
    
    def step(self):
        a0 = self.get_int()
        self.a -= self.b*a0
        
        new_den = self.root - self.a*self.a
        assert new_den % self.b == 0
        new_den /= self.b
        self.a = -self.a
        self.b = new_den
        return a0
    
    def __str__(self):
        return "(sqrt%i + %i)/%i" %(self.root,self.a,self.b)
    
    def key(self):
        return (self.a,self.b)
    
def is_square(N):
    root = int(math.sqrt(N))
    return root*root == N or (root+1)*(root+1) == N
    
def solve(N):
    mem = {}
    num = Num(N)
    i = 0
    while True:
        #print num
        if mem.has_key(num.key()):
            return i-mem[num.key()]
        mem[num.key()] = i
        a = num.step()
        #print a
        i += 1
        
ans = 0
for N in xrange(2,10001):
    if is_square(N):
        continue
    #print N
    period = solve(N)
    ans += period%2
    
print ans