# Reversing a number
n=145
test=0
while n>0:
    r=n%10
    test=test*10+r
    n=n//10

print(test)