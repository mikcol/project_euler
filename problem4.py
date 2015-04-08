
def is_palindrome(number):

    num_str = str(number)
    rev_str = num_str[::-1]
    if num_str == rev_str:
        return True
    else:
        return False


a = 1
b = 1
pal = 0 
while True:
    temp = a * b

    if is_palindrome(temp) and temp > pal:
        pal = temp
    a+=1
    if a > 999:
        if b > 999:
            break
        else:
            a = 1
            b+=1
    
print pal
