# ScoreSaber CLI

import requests
import json

SCORESABER_API = "https://scoresaber.com/api"

def start():
    startReqList = ["1", "2", "3", "4"]
    print("ScoreSaber CLI\nby Parapass\n\nPress Ctrl+C to exit at any time\n\nSelect an option:\n1 - Get User (SteamID)\n2 - Get Map (ScoreSaber Hash)\n3 - Limited Request Library Testing\n4 - Quit Program")
    # this print statement makes me wanna 'sudo rm -rf / --no-preserve-root' myself
    startReq = input(">>> ");
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
    if "errorMessage" in response:
        print(f'Error: {response["errorMessage"]}. Please re-enter your SteamID.\n')
        getUser()
    else:
        print(f'Name - {response["name"]}')
        print(f'Country - {response["country"]}')
        print(f'Global Rank - #{response["rank"]}')
        print(f'Country Rank - #{response["countryRank"]}')
        print(f'PP (Performance Points) - {response["pp"]}')
        print(f'Total Score - {response["scoreStats"]["totalScore"]}')
        print(f'Total Ranked Score - {response["scoreStats"]["totalRankedScore"]}')
        print(f'Total Play Count - {response["scoreStats"]["totalPlayCount"]}')
        print(f'Ranked Play Count - {response["scoreStats"]["rankedPlayCount"]}')
    # most optimized python code to ever exist
    scoreConfirm = input("Would you like to see the top scores of this user? (y/n)\n>>> ")
    if scoreConfirm == "y":
        scoreResp = requests.get(f"{SCORESABER_API}/player/{steamID}/scores?limit=10&sort=top").json()
        for score in scoreResp["playerScores"]:
            print(f'\nSong Name - {score["leaderboard"]["songName"]}')
            print(f'Song Author - {score["leaderboard"]["songAuthorName"]}')
            print(f'Level Creator - {score["leaderboard"]["levelAuthorName"]}')
            print(f'Rank - {score["score"]["rank"]}')
            print(f'Score - {score["score"]["modifiedScore"]}')
            # we want to use modified score here because what if their top play is overkill DAFS??? HUH????
            print(f'PP - {score["score"]["pp"]}')
        # didnt work ima use chatgpt
        # I GOT IT HIP HIP HOORAY!
        input("Press Enter to continue...")
        start()
    elif scoreConfirm == "n":
        print("Returning to main screen...\n")
        start()
        # rip debug mode we done did kil it :(

def getMap():
    leaderboardID = input("Enter ScoreSaber Leaderboard ID (usually a 6 digit number)\n>>> ")
    mapResponse = requests.get(f"{SCORESABER_API}/leaderboard/by-id/{leaderboardID}/info").json()
    print(mapResponse)
    start()

def limitedTest():
    # just the same code from above but it doenst parse the json!!!
    print("Testing not needed at the moment. Returning to main screen...\n")

start();
