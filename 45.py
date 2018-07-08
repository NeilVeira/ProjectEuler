import math

def is_pent(x):
    det = 1 + 24*x
    det_root = int(math.sqrt(det))
    if (det_root+1)**2 == det:
        det_root += 1
    
    n = (1 + det_root)/6
    
    return n*(3*n-1)/2 == x

def is_hex(x):
    det = 1+8*x
    det_root = int(math.sqrt(det))
    if (det_root+1)**2 == det:
        det_root += 1
    
    n = (1+det_root)/4
    return n*(2*n-1) == x 

i = 286
while True:
    tri = i*(i+1)/2
    if is_pent(tri) and is_hex(tri):
        print tri
        break
    i += 1