import psutil
from datetime import datetime
import time
import json
import threading
import datetime
from datetime import date
import AFK_timer

AFK_TIMEOUT = 5
game_on = False
LOG_File = "H:\\Work.exe\\M SHI\\game_sessions.json"
total_afk_time=0

fortnite_process="FortniteClient-Win64-Shipping.exe"
valorant_process="VALORANT-Win64-Shipping.exe"
finals_process="Discovery.exe"
test_process="NZXT CAM.exe"

all_processes = frozenset({fortnite_process,valorant_process,finals_process,test_process})

def is_game_running(game_name):
    for process in psutil.process_iter():
        if process.name() == game_name:
            return True
    return False
    
def inactive():
    while game_on == True:
        #afk code
        time.sleep(3)
        if game_on==False:
            print("done")
            break

def time_game(game_name):
    global game_on
    if is_game_running(game_name)==False:
        print("No game is running")
    else:
        start_time = time.time()
        game_on=True
        time.sleep(3)
        t = threading.Thread(target=inactive)
        t.start()
        print("game started")
        while(is_game_running(game_name)==True):
            

            end_time = time.time()      
        game_on=False
        played = end_time-start_time
        print(f"Session was on for: {played:.2f} seconds")
        time_played= played-total_afk_time
        print(f"Actual play time: {time_played:.2f} seconds")
        with open (LOG_File,'r') as f:
            yaa=json.load(f)
            yaa[game_name][0]["lastplayed"]=str(date.today())
            yaa[game_name][0]["lastsess"]=int(time_played)
            yaa[game_name][0]['playtime']=yaa[game_name][0]['playtime']+int(time_played)

        with open(LOG_File,'w') as f:
            json.dump(yaa,f,indent=4)

#print(time_game(fortnite_process))
def check_is_running():
    for a in all_processes:
        if is_game_running(a)==True:
            print(a, "is running rn cuh")
            print(time_game(a))
    print("no game is running cuh")
check_is_running()
