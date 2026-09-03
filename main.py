import http.client
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("HOCKEY_API_KEY")

conn = http.client.HTTPSConnection("v1.hockey.api-sports.io")

headers = {
    'x-apisports-key': api_key
    }

conn.request("GET", "/teams?id=132", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))