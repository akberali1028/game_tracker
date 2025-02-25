import json
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import gametracker

info_file = gametracker.LOG_File


val="Valorant"
fn="Fortnite"
test="NZXT Cam"
finals="The Finals"
gnames = [val, fn, finals, test]

with open(info_file, 'r') as f:
    allinf = json.load(f)

totaltesttime = allinf['NZXT CAM.exe'][0]['playtime']
totalvaltime = allinf["Discovery.exe"][0]['playtime']
totalfinalstime = allinf["VALORANT-Win64-Shipping.exe"][0]['playtime']
totalfntime = allinf["FortniteClient-Win64-Shipping.exe"][0]['playtime']

def getllg(gamename):
    return f"Info for {gamename} \n Total time is : {disp(allinf[gamename][0]['playtime'])}\n Last session was: {disp(allinf[gamename][0]['lastsess'])}\n Last played : {allinf[gamename][0]['lastplayed']}\n Goal : {disp(allinf[gamename][0]['Goal'])}\n"

alldatotal = (totalfinalstime + totaltesttime + totalfntime + totalvaltime) / 3600
game_times = {
    "Valorant": totalfinalstime // 3600,
    "Fortnite": totalfntime // 3600,
    "The Finals": totalvaltime // 3600,
    "NZXT Cam": totaltesttime // 3600
}


def disp(gametime):
    if gametime < 3600:
        return f" {gametime // 60} Minutes"
    elif gametime < 86400:
        return f" {gametime // 3600} hours {int(((gametime / 3600) - (gametime // 3600)) * 60)} Minutes"
    else:
        return f" {gametime // 86400} days {int(((gametime / 86400) - (gametime // 86400)) * 24)} Hours"



print(f"total time played : {alldatotal:.1f} hours\n")



def writegoal(gamename):
    goal = int(input("enter your goal for the game in minutes: "))
    allinf[gamename][0]["Goal"]=int(goal*60)

    with open(info_file,'w') as f:
        json.dump(allinf,f,indent=4)

for i in gametracker.all_processes:
    print(getllg(i))



def set_game_goal():
    print("Select a game to set a goal:")
    print("1. Valorant")
    print("2. Fortnite")
    print("3. NZXT Cam")
    print("4. Discovery")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            writegoal("VALORANT-Win64-Shipping.exe")
        case "2":
            writegoal("FortniteClient-Win64-Shipping.exe")
        case "3":
            writegoal("NZXT CAM.exe")
        case "4":
            writegoal("Discovery.exe")
        case _:
            print("Invalid choice, please try again.")

set_game_goal()

