import tkinter as tk
from win11toast import notify
from winsound import PlaySound, SND_ALIAS, SND_ASYNC


def startPomodoro():
    global isRunning
    isRunning = True
    startButton.configure(state="disabled")
    stopButton.configure(state="normal")
    update()

def stopPomodoro():
    global isRunning
    startButton.configure(state="normal")
    stopButton.configure(state="disabled")
    isRunning = False

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
    else:
        # Stop the timer
        try:
            root.after_cancel(timerLoop)
        except:
            print("Timer is stopped/not running")
root = tk.Tk()

isRunning = None
soundPath = "sounds/defaultsound.wav"
time = 10
name = "aklsdfkljaslkjdf"
timeText = "%02d:%02d" % (int(time / 60), time % 60)
timeLabel = tk.Label(root, text=timeText)
timeLabel.pack()

startButton = tk.Button(root, text="Start", command=startPomodoro)
startButton.pack()
stopButton = tk.Button(root, text="Stop", command=stopPomodoro, state="disabled")
stopButton.pack()


root.mainloop()
