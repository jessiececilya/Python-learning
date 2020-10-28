str="aec"
count1={}
# vowels=["a","e","i","o","u"]
# l=list(str)
# print(l)

            # print(count)
            
            # for vowels in str:
    # count=count+1
# print(count)
for vowel in "aeiou":
    c1=str.count(vowel)
    count1[vowel]=c1
    c2=count1.values()
    #print(count1.values())
    total_vowels=sum(c2)
print(count1)
print(total_vowels)