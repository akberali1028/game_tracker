import psutil
from datetime import datetime
import time
import json
from pynput.mouse import Listener as MouseListener # type: ignore
from pynput.keyboard import Listener as KeyboardListener # type: ignore
import datetime
from datetime import date

"""games_on = []
LOG_File = "game_sessions.json"
afk_time=120

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

def time_game(game_name):
    start_time = 0
    end_time = 0

    if is_game_running(game_name)!=True:
        print("No game is running")
    else:
        start_time = time.time()
        print("game started")
        while(is_game_running(game_name)!=False):
            time.sleep(5)
            if(is_game_running(game_name)==False):
                end_time = time.time()
                print(end_time)
        time_played = end_time-start_time
        print(f"Session was on for: {time_played:.2f} seconds")

        with open (LOG_File,'r') as f:
            yaa=json.load(f)
            print(yaa)
            
            yaa[game_name]=yaa[game_name]+int(time_played)
        print(yaa)

        with open(LOG_File,'w') as f:
            json.dump(yaa,f,indent=4)

#print(time_game(fortnite_process))
def check_is_running():
    for a in all_processes:
        if is_game_running(a)==True:
            print(a, "is running rn cuh")
            print(time_game(a))
    else: print("no game is running cuh")
check_is_running()
"""


print(date.today())