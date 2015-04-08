fib = [1,2]
num = 0
lim = 4*10**6
total = 2
while num < lim:
    num = fib[-2]+fib[-1]
    if num > lim:
        break
    fib.append(num)
    if num % 2 == 0:
        total += num

print total
