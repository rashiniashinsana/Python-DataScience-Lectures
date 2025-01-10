import requests 

response = requests.get('https://api.github.com/events')

print(response)
print(response.status_code)

