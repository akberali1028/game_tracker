import json
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# Load game session data
info_file = "H:\\Work.exe\\M SHI\\game_sessions.json"

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

# Convert to hours
alldatotal = (totalfinalstime + totaltesttime + totalfntime + totalvaltime) / 3600
game_times = {
    "Valorant": totalfinalstime // 3600,
    "Fortnite": totalfntime // 3600,
    "The Finals": totalvaltime // 3600,
    "NZXT Cam": totaltesttime // 3600
}


def disp(gametime, gamename):
    if gametime < 3600:
        return f"Total time {gamename} played: {gametime // 60} Minutes"
    elif gametime < 86400:
        return f"Total time {gamename} played: {gametime // 3600} hours {int(((gametime / 3600) - (gametime // 3600)) * 60)} Minutes"
    else:
        return f"Total time {gamename} played: {gametime // 86400} days {int(((gametime / 86400) - (gametime // 86400)) * 24)} Hours"



print(f"total time played : {alldatotal:.1f} hours")



def writegoal(gamename):
    goal = int(input("enter your goal for the game in minutes: "))
    allinf[gamename][0]["Goal"]=int(goal*60)

    with open(info_file,'w') as f:
        json.dump(allinf,f,indent=4)


print(disp(totaltesttime,test))
writegoal('NZXT CAM.exe')


