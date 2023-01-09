# API-Template
This is a template for creating a basic API using Django

## Calling the API
```py
import json
import requests

url = 'http://127.0.0.1:8000/api/fullname/'

payload = {
    "name" : "Ritik",
    "lastname" : "Chahar"
    }

headers = {'content-type': 'application/json'}

response = requests.post(url, json = payload, headers = headers).json()
print(response)
```
### Response
```json
{
   "Answer":"Your name is Ritik Chahar"
}
```
