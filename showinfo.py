import json
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

info_file="game_sessions.json"

with open(info_file, 'r') as f:
    allinf=json.load(f)


totaltesttime=allinf['NZXT CAM.exe'][0]['playtime']
totalvaltime=allinf["Discovery.exe"][0]['playtime']
totalfinalstime=allinf["VALORANT-Win64-Shipping.exe"][0]['playtime']
totalfntime=allinf["FortniteClient-Win64-Shipping.exe"][0]['playtime']

alldatotal= totalfinalstime+totaltesttime+totalfntime+totalvaltime

val="Valorant"
fn="Fortnite"
test="NZXT Cam"
finals="The Finals"

def button1_action():
    new_window = tk.Toplevel()  # Create a new window
    new_window.title("New Window")
    new_window.geometry("300x200")
    tk.Label(new_window, text="This is the new UI").pack(pady=20)

def button2_action():
    print("Button 2 clicked!")

def button3_action():
    print("Button 3 clicked!")
    
def button4_action():
    print("Button 4 clicked!")

def show_chart():
    gnames = [val, fn, finals, test]
    gtimes = [totalfinalstime // 3600, totalfntime // 3600, totalvaltime // 3600, totaltesttime // 3600]
    
    # Create the pie chart with a matching background color
    fig, ax = plt.subplots(facecolor="#1A1B1A")
    ax.pie(gtimes, labels=gnames, autopct=lambda p: '{:.0f}'.format(p * sum(gtimes) / 100))
    ax.set_title('Total Game Time in hours:', color="white")
    ax.set_facecolor("#1A1B1A")
    for text in ax.texts:
        text.set_color("white")

    
    # Embed the chart in the Tkinter window
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    
    # Display the result of disp function under the chart
    total_time_label = tk.Label(chart_frame, text=disp(alldatotal, ""), fg="white", bg="#1A1B1A", font=("Arial", 12))
    total_time_label.pack(side=tk.BOTTOM, pady=10)

def disp(gametime, gamename):
    if gametime < 3600:
        return f"Total time {gamename} played: {gametime // 60} Minutes"
    elif gametime < 86400:
        return f"Total time {gamename} played: {gametime // 3600} hours {int(((gametime / 3600) - (gametime // 3600)) * 60)} Minutes"
    else:
        return f"Total time {gamename} played: {gametime // 86400} days {int(((gametime / 86400) - (gametime // 86400)) * 24)} Hours"

root = tk.Tk()
root.geometry("+370+200")
root.minsize(750, 500)
root.configure(background="#1A1B1A")

# Create a chart frame at the top
chart_frame = tk.Frame(root, bg="#1A1B1A", height=300)
chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Separator line
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill=tk.X, pady=5)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#1A1B1A", height=200)
button_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Load images for buttons

# Add buttons with images
btn1 = tk.Button(button_frame, image=img1, command=button1_action, bg="#1A1B1A", borderwidth=0)
btn1.pack(side=tk.LEFT, padx=10, pady=10)

btn2 = tk.Button(button_frame, image=img2, command=button2_action, bg="#1A1B1A", borderwidth=0)
btn2.pack(side=tk.LEFT, padx=10, pady=10)

btn3 = tk.Button(button_frame, image=img3, command=button3_action, bg="#1A1B1A", borderwidth=0)
btn3.pack(side=tk.LEFT, padx=10, pady=10)

btn4 = tk.Button(button_frame, image=img4, command=button4_action, bg="#1A1B1A", borderwidth=0)
btn4.pack(side=tk.LEFT, padx=10, pady=10)

show_chart()  # Automatically display the chart when the GUI opens
root.mainloop()

