num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

gcds = []
def gcdCheck(b,c):
    if b > c:
        high = b
    else: 
        high = c
    for k in range(1, high+1):
        if b%k == 0 and c%k == 0:    
            gcds.append(k)
    return max(gcds)




print(f"GCD of {num1} and {num2} is:",gcdCheck(num2, num1))



def lcmCheck(b,c):

    if b > c:
        high = b
    else:
        high = c
    for u in range(high+1, 2, -1):
        if b%u == 0 and c%u == 0:
            return u*(b//u)*(c//u)
    else:
        return b * c

    
print(f"LCM of {num1} and {num2} is:",lcmCheck(num2, num1))

