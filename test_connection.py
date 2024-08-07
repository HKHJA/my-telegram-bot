import requests

# The bot token provided
url = 'https://api.telegram.org/bot7284156733:AAHUpfjB65s7C-ciuHZP8eEM_BgId4-yGTA/getMe'
response = requests.get(url)
print(response.json())
