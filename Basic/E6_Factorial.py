# Factorial of number
num=7
f=1
if num<0:
    print("Not a factorial")
elif num==0:
    print("Factorial is 1")
else:
    for i in range (1,num+1):
        f=f*i
    print("Factorial is f",f)