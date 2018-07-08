import math

def get_digits(num):
    digits = []
    while num > 0:
        digits.append(num%10)
        num /= 10
    digits.reverse()
    return digits

def get_convergent(seq):
    num = 0
    den = 1
    for i in reversed(range(len(seq))):
        num += den*seq[i]
        num,den = den,num
    return den,num

seq = [2,1]
for i in xrange(1,100):
    seq.extend([2*i,1,1])

num,den = get_convergent(seq[:100])
print sum(get_digits(num))