"""
Event:IBM Hack challenge 2020
@team members: Barathkumar G  id:191cs138
               Ajay S         id:191cs110
               Dhanush s      id:191cs156
Guide name: Ms Malathi T AP/CSE
Mentor name : Mr Hemant Kumar Gahlot   AI Developer/IBM
              Ms Gayatri   AI Developer/IBM
"""
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'windspeed':2, 'wind direction':4 })

print(r.json())