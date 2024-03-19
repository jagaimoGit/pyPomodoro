import tkinter as tk
from win11toast import notify
from winsound import PlaySound, SND_ALIAS, SND_ASYNC


def update(soundPath, name="DEFAULT"):
    global time, timeText    
    if time > 0:
        time -= 1
        timerCall = root.after(1000, update, soundPath)
    if time == 0:
        root.after_cancel(timerCall)
        PlaySound(soundPath, SND_ALIAS|SND_ASYNC)
        notify("Pomodoro Timer", f"Timer from {name} is done!", audio={'silent': 'true'})
    timeText = "%02d:%02d" % (int(time / 60), time % 60)
    timeLabel.configure(text=timeText)
    print(timeText)

soundPath = "sounds/defaultsound.wav"
root = tk.Tk()

time = 10
timeText = "%02d:%02d" % (int(time / 60), time % 60)
timeLabel = tk.Label(root, text=timeText)
timeLabel.pack()

timerCall = root.after(1000, update, soundPath)

root.mainloop()