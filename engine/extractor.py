import datetime
from engine.database import update_location
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

    # Make 5 captures at a 5 second interval and get the average
    average_cars = 0
    for i in range(5):
        filename = "capture_" + str(datetime.datetime.now().timestamp()) + ".png"
        engine.capture(video, filename)
        # Get the total number of cars in the image
        total_cars = detection.count_total_vehicles("captures/"+filename)
        average_cars += total_cars
        sleep(5)

    average_cars = average_cars / 5
    driver.quit()
    

    print("Saved capture to " + filename)



    location_data = {
        "id": location["id"],
        "name": location["name"],
        "traffic": average_cars,
        "timestamp": datetime.datetime.now().timestamp(),
        "longitude": location["longitude"],
        "latitude": location["latitude"],
        "link": location["yt_live"]
    }

    update_location(location_data)

    print(location_data)