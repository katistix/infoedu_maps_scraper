import engine.engine as engine
from time import sleep


# driver = engine.initialize("https://www.youtube.com/watch?v=ByED80IKdIU&ab_channel=CityofColdwaterMI")
driver = engine.initialize("https://www.youtube.com/watch?v=rs2be3mqryo&ab_channel=ULTRAVISIONCONSULT")

sleep(3)

video = engine.getVideoElement(driver)



# Capture 20 screenshots at a rate of 2 seconds
for i in range(5):
    engine.capture(video, f"video{i}.png")
    sleep(2)

input("Press enter to exit")