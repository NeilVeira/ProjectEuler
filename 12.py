n = 1
while True:
    tri = n*(n+1)/2
    div = 0
    i = 1
    while i*i <= tri:
        if tri%i == 0:
            if i*i == tri:
                div += 1
            else:
                div += 2
        i += 1
        
    #print tri,div
    if div >= 500:
        break
    
    n += 1
    
print tri