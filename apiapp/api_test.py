import requests
import json
from itertools import islice
food = [{"a":"A"}, {"b":"b"}, {"c":"c"}]
for i in food:
    print(i)
a = ['w', '2']
b = islice(a, 1)
for i in b:
    print(i)

