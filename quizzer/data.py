from argon2 import Parameters
import requests

url="https://opentdb.com/api.php"

Parameters={'amount':10,
            'difficulty':'medium',
            'type':'multiple'}

response=requests.get(url,params=Parameters)
response.raise_for_status()
data=response.json()
question_data=data['results']

