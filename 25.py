digit1000 = 10**999
fib1 = 1
fib2 = 1
i = 2
while fib2 < digit1000:
    fib1,fib2 = fib2,fib1+fib2
    i += 1
print i