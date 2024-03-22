import tkinter as tk
from win11toast import notify
from winsound import PlaySound, SND_ALIAS, SND_ASYNC
import function


def startPomodoro():
    global isRunning
    isRunning = True
    print(f"Starting the timer {name}!")
    startButton.configure(state="disabled")
    stopButton.configure(state="normal")
    resetButton.configure(state="disabled")
    update()

def stopPomodoro():
    global isRunning
    startButton.configure(state="normal")
    stopButton.configure(state="disabled")
    resetButton.configure(state="normal")
    isRunning = False

def resetTimer():
    global profile, x, time
    time = profile[str(x)]["time"]
    timeText = "%02d:%02d" % (int(time / 60), time % 60)
    timeLabel.configure(text=timeText)

def switchProfiles():
    global profile, x, time, name, soundPath
    if (x + 1) < len(profile):
        x += 1
    else:
        x = 0
    time = profile[str(x)]["time"]
    name = profile[str(x)]["name"]
    soundPath = profile[str(x)]["soundPath"]
    timeText = "%02d:%02d" % (int(time / 60), time % 60)
    timeLabel.configure(text=timeText)
    

def update():
    global soundPath, name, time, timeText, isRunning
    if isRunning:
        if time > 0:
            time -= 1
            timeText = "%02d:%02d" % (int(time / 60), time % 60)
            timeLabel.configure(text=timeText)
            print(timeText)
            timerLoop = root.after(1000, update)  # Schedule the next update
        else:
            # Timer is done
            PlaySound(soundPath, SND_ALIAS | SND_ASYNC)
            notify("Pomodoro Timer", f"Timer from {name} is done!", audio={'silent': 'true'})
            switchProfiles()
            startButton.configure(state="normal")
            stopButton.configure(state="disabled")
            resetButton.configure(state="normal")
            isRunning = False
    else:
        # Stop the timer
        try:
            root.after_cancel(timerLoop)
        except:
            print("Timer is stopped/not running")
root = tk.Tk()

profile = function.loadProfile()

x = 0
time = profile[str(x)]["time"]
name = profile[str(x)]["name"]
soundPath = profile[str(x)]["soundPath"]

isRunning = None
timeText = "%02d:%02d" % (int(time / 60), time % 60)
timeLabel = tk.Label(root, text=timeText)
timeLabel.pack()

startButton = tk.Button(root, text="Start", command=startPomodoro)
startButton.pack()
stopButton = tk.Button(root, text="Pause", command=stopPomodoro, state="disabled")
stopButton.pack()
resetButton = tk.Button(root, text="Reset", command=resetTimer)
resetButton.pack()

root.mainloop()
