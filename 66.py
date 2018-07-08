import math

def solve(D):
    x = 2
    while True:
        if (x*x-1)%D == 0:
            target = (x*x-1)/D
            y = int(math.sqrt(target))
            if y*y == target or (y+1)*(y+1) == target:
                return x
        x += 1
        
def is_square(N):
    root = int(math.sqrt(N))
    return root*root == N or (root+1)*(root+1) == N


def continued_fraction(N):
    '''
    Compute the continued fraction of N where N is a positive integer
    and not a perfect square. 
    Returns a list of the continued fraction terms [a0,a1,...] and an 
    integer for the seuqnece period. 
    '''
    root = int(math.sqrt(N))
    #N must not be a perfect square
    assert root*root != N and (root+1)*(root+1) != N 
    
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
    
    mem = {}
    num = Num(N)
    i = 0
    seq = []
    while True:
        #print num
        if mem.has_key(num.key()):
            return seq, i-mem[num.key()]
        mem[num.key()] = i
        a = num.step()
        seq.append(a)
        #print a
        i += 1
        
def solve(D):
    a,period = continued_fraction(D)
    #print a,period
    #r = len(a)-1
    #print r
    
    #compute convergent numerators (p) and denominators (q)
    p = [a[0], a[0]*a[1]+1]
    q = [1,a[1]]
    for i in xrange(2,len(a)):
        p.append(a[i]*p[i-1] + p[i-2])
        q.append(a[i]*q[i-1] + q[i-2])
        if p[-1]*p[-1] - D*q[-1]*q[-1] == 1:
            return p[-1],q[-1]
    #print p
    #print q    
    
    while True:
        a.append(a[-period])
        p.append(a[-1]*p[-1] + p[-2])
        q.append(a[-1]*q[-1] + q[-2])
        if p[-1]*p[-1] - D*q[-1]*q[-1] == 1:
            return p[-1],q[-1]
    
    print a
    print p
    print q
    #return p[-1],q[-1]
    
ans = 2
biggest = 0
for D in xrange(2,1001):
    if not is_square(D):
        #print D
        x,y = solve(D)
        #print x,y
        assert x*x - D*y*y == 1
        if x > biggest:
            biggest = x
            ans = D
            
print ans
