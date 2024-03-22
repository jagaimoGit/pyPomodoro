

def createDefaultProfile(defprofile: dict):
    profileDetails = []
    for key in defprofile.keys():
        profileDetails.append([key, defprofile[key]["name"], defprofile[key]["time"], defprofile[key]["soundPath"]])
    with open("timerProfile.csv", "w") as wf:
        for ls in profileDetails:
            wf.write(f"{ls[0]},{ls[1]},{ls[2]},{ls[3]}\n")
#Example dictionary
defprofile = {
    "0": {
        "name": "Work",
        "time": 120,
        "soundPath": "sounds/defaultsound.wav"
    },
    "1": {
        "name": "Break",
        "time": 120,
        "soundPath": "sounds/defaultsound.wav"
    },
    "2": {
        "name": "Long Break",
        "time": 120,
        "soundPath": "sounds/defaultsound.wav"
    },
}

createDefaultProfile(defprofile)
