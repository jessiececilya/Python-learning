# String Reversal/ Palindrome check
str="a2C2a"
mystr=str.casefold()
# print(list(mystr))
revstr=reversed(mystr)
rev="".join(revstr)
print(rev)
print(mystr)

if ((mystr)==(rev)):
    print("Yes")
else:
    print("No")