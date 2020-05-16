import requests

url = 'localhost:8888/sendImage'
r = requests.post(url, data="UBMk30rjy0o.jpg".encode('utf-8'))
print(r.text)