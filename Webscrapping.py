import requests
url = ('http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=18b9bbcbf44742ca83ac882fb35a7ac9') 
response = requests.get(url)
a=response.json()
# print (response.json())
for i in range(0,5):
    print("Heading name "+str(i+1)+" is")
    print(a['articles'][i]['title'])
    print(a['articles'][i]['url'])
    print(a['articles'][i]['urlToImage'])
    print(a['articles'][i]['publishedAt'])