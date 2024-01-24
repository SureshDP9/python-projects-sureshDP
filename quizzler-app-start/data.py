import requests

parameters = {
   "amount": 10,
   "category": 9,
   "difficulty": "easy",
   "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php",params=parameters)
dataList = response.json()["results"]
question_data = dataList
