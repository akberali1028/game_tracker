import psutil
from datetime import datetime
import time
import json
from pynput.mouse import Listener as Listener 

import datetime
from datetime import date

AFK_TIMEOUT = 5
last_mouse_activity = time.time()
is_afk = False
afk_start_time = 0
total_afk_time = 0
game_on = False
LOG_File = "game_sessions.json"

fortnite_process="FortniteClient-Win64-Shipping.exe"
valorant_process="VALORANT-Win64-Shipping.exe"
finals_process="Discovery.exe"
test_process="NZXT CAM.exe"

all_processes = frozenset({fortnite_process,valorant_process,finals_process,test_process})

def on_move(x, y):
    global last_mouse_activity
    last_mouse_activity = time.time()

def on_click(x, y, button, pressed):
    global last_mouse_activity
    last_mouse_activity = time.time()

# Function to check AFK status
def check_afk():
    global last_mouse_activity
    return (time.time() - last_mouse_activity) > AFK_TIMEOUT

# AFK tracking loop
def track_afk():
    global is_afk, afk_start_time, total_afk_time
    while True:
        if check_afk():
            if not is_afk:  # User just became AFK
                print("User is AFK")
                afk_start_time = time.time()
                is_afk = True
        else:
            if is_afk:  # User just came back
                afk_end_time = time.time()
                afk_duration = afk_end_time - afk_start_time
                total_afk_time += afk_duration
                print(f"User is back. AFK duration: {afk_duration:.2f} seconds")
                is_afk = False
            
        time.sleep(1)   

def is_game_running(game_name):
    
    for process in psutil.process_iter():
        if process.name() == game_name:
            return True
    return False
    
def time_game(game_name):
    if is_game_running(game_name)==False:
        print("No game is running")
    else:
        start_time = time.time()
        print("game started")
        while(is_game_running(game_name)==True):
            end_time = time.time()        
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
