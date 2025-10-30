import requests

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
                "name": game["name"],
                "playtime": game["playtime_forever"],
                "icon_url": game["img_icon_url"]
            })
        return sanitizedGames