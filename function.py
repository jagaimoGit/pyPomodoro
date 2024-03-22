

def createDefaultProfile(defprofile: dict):
    profileDetails = []
    for key in defprofile.keys():
        profileDetails.append([key, defprofile[key]["name"], defprofile[key]["time"], defprofile[key]["soundPath"]])
    with open("timerProfile.csv", "w") as wf:
        for ls in profileDetails:
            wf.write(f"{ls[0]},{ls[1]},{ls[2]},{ls[3]}\n")

def loadProfile():
    profiles = {}
    try:
        with open("timerProfile.csv", "r") as rf:
            ls = rf.readlines()
            for item in ls:
                item = item.rstrip("\n")
                item = item.split(",")
                profiles[item[0]] = {
                    "name": item[1],
                    "time": int(item[2]),
                    "soundPath": item[3]
                }
        return profiles
    except:
        global defprofile
        createDefaultProfile(defprofile)
        loadProfile()

#Example dictionary
defprofile = {
    "0": {
        "name": "Work",
        "time": 10,
        "soundPath": "sounds/defaultsound.wav"
    },
    "1": {
        "name": "Break",
        "time": 5,
        "soundPath": "sounds/defaultsound.wav"
    },
    "2": {
        "name": "Long Break",
        "time": 3,
        "soundPath": "sounds/defaultsound.wav"
    },
}
