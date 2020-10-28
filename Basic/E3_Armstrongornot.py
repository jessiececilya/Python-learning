# List of Armstrong numbers
l=4
u=2000
for num in range (l,u+1):
    order=len(str(num))
    sum=0
    t=num
    while t>0:
        x=t%10
        sum += x ** order
        t//=10
    if num==sum:    
        print(num)
    
