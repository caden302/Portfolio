import requests
import json

class SteamGrabber:
    def __init__(self, key, url, id):
        self.key = key
        self.url = url
        self.id = id

    def testingURL(self):
        self.url = self.url.replace("<interface name>", "IPlayerService").replace("<method name>", "GetOwnedGames").replace("<version>", "v0001").replace("<steamid>", self.id).replace("<api key>", self.key)
        print(self.url)

    def getSteamJSON(self):
        self.url = self.url.replace("<interface name>", "IPlayerService").replace("<method name>", "GetOwnedGames").replace("<version>", "v0001").replace("<steamid>", self.id).replace("<api key>", self.key)
        response = requests.get(self.url)
        data = response.json()
        games = data["response"]["games"]
        sanitizedGames = []
        for game in games:
            sanitizedGames.append({
                "appid": game["appid"],
                "name": game["name"],
                "playtime": int(game["playtime_forever"]/60),
                "icon_url": game["img_icon_url"]
            })
        sanitizedGames = sorted(sanitizedGames, key=lambda x: x["playtime"], reverse=True)[:5]
        return sanitizedGames