
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'windspeed':2, 'wind direction':4 })

print(r.json())
