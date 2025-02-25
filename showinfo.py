import json
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import gametracker

info_file = gametracker.LOG_File

gametracker.all_processes

val="Valorant"
fn="Fortnite"
test="NZXT Cam"
finals="The Finals"
gnames = [val, fn, finals, test]

with open(info_file, 'r') as f:
    allinf = json.load(f)

# Extract playtime (in seconds)
totaltesttime = allinf['NZXT CAM.exe'][0]['playtime']
totalvaltime = allinf["Discovery.exe"][0]['playtime']
totalfinalstime = allinf["VALORANT-Win64-Shipping.exe"][0]['playtime']
totalfntime = allinf["FortniteClient-Win64-Shipping.exe"][0]['playtime']

def getllg(gamename):
    return f"Info for {gamename} \n \n  last session was: {disp(allinf[gamename][0]['lastsess'])}\nlast played : {allinf[gamename][0]['lastplayed']}\nGoal : {disp(allinf[gamename][0]['Goal'])}"
# Convert to hours
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



print(f"total time played : {alldatotal:.1f} hours")



def writegoal(gamename):
    goal = int(input("enter your goal for the game in minutes: "))
    allinf[gamename][0]["Goal"]=int(goal*60)

    with open(info_file,'w') as f:
        json.dump(allinf,f,indent=4)

for i in gametracker.all_processes:
    print(getllg(i))



