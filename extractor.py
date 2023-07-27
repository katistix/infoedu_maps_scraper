import datetime
from database import update_location
import engine.engine as engine
import engine.detection as detection
from time import sleep


def extractor(location):
    driver = engine.initialize(location['yt_live'])

    if driver == None:
        print("Failed to initialize driver")
        return
    
    sleep(3)

    video = engine.getVideoElement(driver)

    # Make a capture
    # Generate a random filename using the current time
    
    filename = "capture_" + str(datetime.datetime.now().timestamp()) + ".png"
    engine.capture(video, filename)

    driver.quit()
    print("Saved capture to " + filename)


    # Get the total number of cars in the image
    total_cars = detection.count_total_vehicles("captures/"+filename)

    location_data = {
        "id": location["id"],
        "name": location["name"],
        "total_cars": total_cars,
        "timestamp": datetime.datetime.now().timestamp(),
        "link": location["yt_live"]
    }

    update_location(location_data)

    print(location_data)