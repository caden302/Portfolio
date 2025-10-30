from dotenv import load_dotenv
import os
from steamGrabber import SteamGrabber
from github_uploader import GitHubUploader
from requests import RequestException

def main():
    load_dotenv()

    key = os.environ["STEAM_API_KEY"]
    url = os.environ["STEAM_API_LINK"]
    id = os.environ["STEAM_ID"]
    path = os.environ["Path_To_Repo"]
    statsJson = os.environ["Path_To_File"]

    grabber = SteamGrabber(key, url, id)
    uploader = GitHubUploader(path, statsJson)

    grabber.testingURL()
    uploader.testUploader()

    try:
        games = grabber.getSteamJSON()
    except RequestException() as e:
        print(e)
    
    if(len(games) > 0):
        uploader.update_json(games)    
    else:
        print("Nothing to update")

if __name__ == "__main__":
    main()