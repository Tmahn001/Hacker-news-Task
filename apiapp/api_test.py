import requests
import json
from itertools import islice
food = [{"a":"A"}, {"b":"b"}, {"c":"c"}]
for i in food:
    print(i.get('a'))
    for a, b in i.items():

        print(a)
a = ['w', '2']
b = islice(a, 1)
for i in b:
    print(i)
url = f'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
response = requests.get(url)
data = response.json()

top_100 = islice(data, 10)
for item in top_100:
    print(item)
    url = f'https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty'
    response = requests.get(url)
    data = response.json()
    print(data)
    if 'kids' in data:
        print(data['kids'])
        for item in data['kids']:
            url = f'https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty'
            response = requests.get(url)
            comment = response.json()
            a = comment.get('text')
            b = comment.get('parent')
            print(a)
            print(b)



