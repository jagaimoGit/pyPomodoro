from configparser import ConfigParser
from time import sleep
from playsound import playsound
from win11toast import toast    

def timer(mins, secs, soundPath, name="DEFAULT"):
    time = mins*60 + secs
    while time > 0:
        time = mins*60 + secs
        if secs < 10:
            print(f"{mins}:0{secs}")
        else:
            print(f"{mins}:{secs}")
        sleep(1)
        if secs == 0:
            mins -= 1
            secs += 59
        else:
            secs -= 1
    playsound(soundPath)
    toast("Pomodoro Timer", f"Timer from {name} is done!")
    

    

timer(0, 3, "sounds/defaultsound.wav")
    
