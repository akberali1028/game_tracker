import psutil
from datetime import datetime
import time
import json
import threading
import datetime
from datetime import date
import AFK_timer
import tkinter as tk
import pygame
game_on = False
LOG_File = "H:\\Work.exe\\M SHI\\game_sessions.json"
sound = "pluh.mp3"

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
class game_runnin:
    def __init__(self,game_name):
        self.game = game_name
    
    def time_game(game):
        global game_on
        with open(LOG_File,'r') as f:
            yaa = json.load(f)
            goal = yaa[game][0]['Goal']
        if is_game_running(game)==False:
            print("No game is running")
        else:
            start_time = time.time()
            game_on=True
            if goal!=0:
                def sound_play():
                    while game_on == True:
                        if (time.time()-start_time>goal):
                            pygame.mixer.init()
                            chime_sound = pygame.mixer.Sound(sound)
                            chime_sound.set_volume(0.3)
                            chime_sound.play()
                            #do whatever after time exceeded the goal
                            break
                        if game_on==False:
                            break
                t = threading.Thread(target=sound_play)
                t.start()
            print("game started")
            while(is_game_running(game)==True):
                end_time = time.time()      
            game_on=False
            played = end_time-start_time #total time played
            print(f"Session was on for: {played:.2f} seconds")
            
            with open (LOG_File,'r') as f:
                yaa=json.load(f)
                yaa[game][0]["lastplayed"]=str(date.today())
                yaa[game][0]["lastsess"]=int(played)
                yaa[game][0]['playtime']=yaa[game][0]['playtime']+int(played)

            with open(LOG_File,'w') as f:
                json.dump(yaa,f,indent=4)

#print(time_game(fortnite_process))
def check_is_running():
    for a in all_processes:
        if is_game_running(a)==True:
            print(a, "is running rn cuh")
            print(game_runnin.time_game(a))
            break
    print("no game is running cuh")

check_is_running()
 
