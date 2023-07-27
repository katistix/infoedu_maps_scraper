# Get json locations from config file
import json
import os
import threading
import time
from datetime import datetime
from engine.extractor import extractor

def getLocations():
    with open("config.json") as config_file:
        config = json.load(config_file)
        return config["locations"]
    


print("Starting...")

locations = getLocations()

# For each location, start a new "extractor" thread,
# If all cores are busy, wait for one to finish, then start a new one,
# Loop through all locations, and repeat every 10 minutes

locations = None

def start_extractor_threads():
    threads = []
    for i, location in enumerate(locations):
        t = threading.Thread(target=extractor, args=(location,))
        threads.append(t)
        t.start()
        if len(threads) == os.cpu_count():
            threads[0].join()
            threads.pop(0)

def loop_extractor_threads():
    while True:
        # Delete all .png files in the captures folder
        for file in os.listdir("captures"):
            if file.endswith(".png"):
                os.remove(os.path.join("captures", file))
                

        start_extractor_threads()
        # After 2 minutes, restart the threads
        time.sleep(120)
    
if __name__ == "__main__":

    locations = getLocations()

    loop_extractor_threads()
