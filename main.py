# Get json locations from config file
import json
import os
import threading
import time
from datetime import datetime


def getLocations():
    with open("config.json") as config_file:
        config = json.load(config_file)
        return config["locations"]
    


print("Starting...")

locations = getLocations()
print("Locations: " + str(locations))

# For each location, start a new "extractor" thread,
# If all cores are busy, wait for one to finish, then start a new one,
# Loop through all locations, and repeat every 10 minutes

# FOR NOW the extractor function will just sleep for 2 minutes, then exit
def extractor():
    print("Starting extractor thread...")
    while True:
        print("Extracting...")
        time.sleep(10)
        print("Done extracting")
        return
    

import json
import os
import threading
import time
from datetime import datetime, timedelta

locations = None

def start_extractor_threads():
    threads = []
    for i, location in enumerate(locations):
        t = threading.Thread(target=extractor)
        threads.append(t)
        t.start()
        if len(threads) == os.cpu_count():
            threads[0].join()
            threads.pop(0)

def loop_extractor_threads():
    while True:
        start_extractor_threads()
        # After 10 minutes, start the threads again
        time.sleep(20)

# FOR NOW the extractor function will just sleep for 2 minutes, then exit
def extractor():
    print("Starting extractor thread...")
    while True:
        print("Extracting...")
        time.sleep(10)
        print("Done extracting")
        return
    
if __name__ == "__main__":

    locations = getLocations()
    print("Locations: " + str(locations))

    loop_extractor_threads()
