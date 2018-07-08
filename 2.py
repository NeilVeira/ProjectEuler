fib1 = 1 
fib2 = 1
ans = 0
while fib2 <= 4000000:
    if fib2%2 == 0:
        ans += fib2
    fib1,fib2 = fib2,fib1+fib2
print ans
