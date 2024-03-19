from configparser import ConfigParser

def createDefaultProfile():
    config = ConfigParser()

    config["PROFILE1"] = {
        "name": "Work",
        "mins": 10,
        "secs": 30,
        "sound": "sounds/defaultsound.wav"
    }

    config["PROFILE2"] = {
        "name": "Rest",
        "mins": 3,
        "secs": 0,
        "sound": "sounds/defaultsound.wav"
    }

    config["PROFILE3"] = {
        "name": "Long Rest",
        "mins": 6,
        "secs": 0,
        "sound": "sounds/defaultsound.wav"
    }

    with open("profile.ini", "w") as f:
        config.write(f)

createDefaultProfile()