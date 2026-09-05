from datetime import date
import http.client

class Team:
    def __init__(self, conn:HTTPSConnection, headers:dict, params:dict):
        self.conn = conn
        self.today = date.today().isoformat()
        self.headers = headers
        self.params = params

        #self.params["season"] = int(date.year) + 1

    def isGame(self):
        print(self.params)

        self.conn.request("GET", f"/games?team={self.params["team"]}&date={self.today}&season=2027", headers=self.headers) #{self.params["season"]}

        response = self.conn.getresponse()
        data = response.read()

        print(data)
        if data["response"]:
            return True
        else:
            return False