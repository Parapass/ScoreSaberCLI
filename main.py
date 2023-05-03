# ScoreSaber CLI

import requests
import json

SCORESABER_API = "https://scoresaber.com/api"

def start():
    startReqList = ["1", "2", "3", "4"]
    print("ScoreSaber CLI\nby Parapass\n\nPress Ctrl+C to exit at any time\n\nSelect an option:\n1 - Get User (SteamID)\n2 - Get Map (ScoreSaber Hash)\n3 - Limited Request Library Testing\n4 - Quit Program")
    # this print statement makes me wanna 'sudo rm -rf / --no-preserve-root' myself
    startReq = input(">>> ")
    while startReq not in startReqList:
        print("Invalid text entered, returning...")
        start()
    if startReq == "1":
        getUser()
    elif startReq == "2":
        getMap()
    elif startReq == "3":
        limitedTest()
    elif startReq == "4":
        # i almost died making this function
        quit()


def getUser():
    steamID = input("Please enter the SteamID of the user you are looking for (example: 76561198335894744)\n>>> ")
    # find a way to make it so you dont have to type 1 bajillion gazillion numbers
    response = requests.get(f"{SCORESABER_API}/player/{steamID}/full").json()
    # most sane python programmer
    print(f'Name - {response["name"]}')
    print(f'Country - {response["country"]}')
    print(f'Global Rank - #{response["rank"]}')
    print(f'Country Rank - #{response["countryRank"]}')
    print(f'PP (Performance Points) - {response["pp"]}')
    print(f'Total Score - {response["scoreStats"]["totalScore"]}')
    print(f'Total Ranked Score - {response["scoreStats"]["totalRankedScore"]}')
    print(f'Total Play Count - {response["scoreStats"]["totalPlayCount"]}')
    print(f'Ranked Play Count - {response["scoreStats"]["rankedPlayCount"]}')
    # actually i probably could use \n to refactor but NAHHHHHH
    scoreConfirm = input("Would you like to see the top scores of this user? (y/n)\n>>> ")
    if scoreConfirm == "y":
        # woopsie diddily doo!
        print("Error: NotImplemented. Please try again later.\n")
        # time to find out how to pull these scores
        # watch it be something dumb like /player/scores
        start()
    elif scoreConfirm == "n":
        print("Returning to main screen...\n")
        start()
    elif scoreConfirm == "db":
        # debug mode for advanced users (me)
        print(f"Full API Response (db) - {response}\n")
        input("Press Enter to continue... ")
        start()

def getMap():
    mapHash = input("Enter ScoreSaber map hash\n>>> ")
    # we need input here but im lazy so i havent added anything here yet
    print("Error: NotImplemented. Please try again later.\n")
    start()

def limitedTest():
    # just the same code from above but it doenst parse the json!!!
    steamID = input("Please enter the SteamID of the user you are looking for (example: 76561198335894744)\n>>> ")
    response = requests.get(f'{SCORESABER_API}/player/{steamID}/full')
    response = response.text
    response = json.loads(response)
    print(response)
    start()

start()
