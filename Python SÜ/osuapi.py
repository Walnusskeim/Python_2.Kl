import requests
import json

client_id = 21799
apikey = "ikpsZepq9MRvtnpN0qJmHdIkuWyaeG7zKiDzNdQ0"

response = requests.get("https://osu.ppy.sh/api/v2/rankings/osu/performance?key=" + apikey)

abc = requests.post(apikey, data = client_id)

print(abc)


print(response)