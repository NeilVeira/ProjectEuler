import math
N = 600851475143
stop = int(math.sqrt(N))
for i in range(2,stop+1):
    while N%i == 0:
        N /= i
        ans = i
print ans