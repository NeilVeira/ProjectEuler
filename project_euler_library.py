import math

def lcm(a,b):
    '''
    Lowest common multiple
    '''
    return a*b/gcd(a,b)

def gcd(a,b):
    '''
    Greatest common divisor
    '''
    if a%b == 0:
        return b
    else: 
        return gcd(b,a%b)

def sieve(MAXN):
    '''
    Sieve of Eratosthenes up to MAXN (inclusive)
    '''
    is_prime = [True]*(MAXN+1)
    for n in xrange(2,MAXN+1):
        if is_prime[n]:
            for mult in xrange(2,MAXN/n+1):
                is_prime[mult*n] = False
    
    primes = []
    for n in xrange(2,MAXN+1):
        if is_prime[n]:
            primes.append(n)
    return primes


def is_prime(n):
    '''
    Check whether n is prime
    '''
    for i in xrange(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def get_digits(num):
    '''
    Return a list of digits of num
    '''
    digits = []
    while num > 0:
        digits.append(num%10)
        num /= 10
    digits.reverse()
    return digits


def is_square(N):
    '''
    Check whether N is a perfect square
    '''
    root = int(math.sqrt(N))
    return root*root == N or (root+1)*(root+1) == N


def phi(n):
    '''
    Compute Euler's totient function
    '''
    if n <= 1:
        return 0
    res = n
    p = 2
    while p*p <= n:
        if n%p == 0:
            res -= res/p
            while n%p == 0:
                n /= p
        p += 1
    if n > 1:
        res -= res/n
    return res 


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
        
        
def generate_phi(MAXN):
    '''
    Generate phi(n) for all phi from 2 to MAXN inclusive. 
    '''
    phi_by_n = [1]*(MAXN+1)
    is_prime = [True]*(MAXN+1)
    
    for i in xrange(2,MAXN+1):
        if is_prime[i]:
            for m in xrange(1,MAXN/i+1):
                phi_by_n[i*m] *= 1-1.0/i
                is_prime[i*m] = False
                
    phi = [0,1]
    for i in range(2,MAXN+1):
        phi.append(int(round(phi_by_n[i]*i)))
    return phi