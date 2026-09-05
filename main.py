import http.client
import os
from dotenv import load_dotenv

from class_files.team import Team

load_dotenv()
api_key = os.getenv("HOCKEY_API_KEY")

conn = http.client.HTTPSConnection("v1.hockey.api-sports.io")

headers = {
    'x-apisports-key': api_key
    }

pce = Team(conn, headers, params={"team": 132})
vse = Team(conn, headers, params={"team": 153})

jeHra = pce.isGame()