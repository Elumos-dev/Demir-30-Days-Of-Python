# Day 28: HTTP and APIs from the client side   (pip install requests)
# GET read | POST create | PUT update | DELETE remove
# Status: 200 OK | 201 Created | 400 Bad request | 404 Not found | 500 Server error
import requests

base = 'https://jsonplaceholder.typicode.com'          # free fake API for practice

r = requests.get(f'{base}/posts/1')
print(r.status_code, r.headers['Content-Type'])        # headers = info about the response
print(r.json()['title'])                               # body

r = requests.post(f'{base}/posts', json={'title': 'hi'})   # json= sends a JSON body
print(r.status_code, r.json())

print(requests.put(f'{base}/posts/1', json={'title': 'new'}).status_code)
print(requests.delete(f'{base}/posts/1').status_code)
