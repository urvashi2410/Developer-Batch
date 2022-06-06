import requests 
from json import dumps 

URL = 'http://127.0.0.1:8000/createstudent/'
data = {
    'name' : 'Pranjal',
    'rollNo' : 12,
    'city' : 'Punjab'
}

# converts python data to json data 
json_data = dumps(data)
response = requests.post(url = URL, data=json_data)
print(response.status_code)