number = 600851475143
temp = number
i = 2
factors = []
while temp>=i:
    if temp % i == 0:
        temp = temp / float(i) 
        factors.append(i)
    else:
        i+=1

print factors
