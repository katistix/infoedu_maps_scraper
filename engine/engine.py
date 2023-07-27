import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

CAPTURE_DIR = "captures/"


def createDriver(headless):
    import undetected_chromedriver as uc
    print("Starting automated browser...")
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    return driver


def initialize(link):
    if link == None:
        print("No link provided")
        return None


    driver = None
    # Try to create a driver, if it fails, try again for 3 times
    for i in range(3):
        try:
            driver = createDriver(True)
            break
        except:
            print("Failed to create driver, trying again...")
            pass

    driver.get(link)
    driver.implicitly_wait(10)


    # The accept cookies button can be either of these two
    # Aria label: Accept all
    # Aria label: Accept the use of cookies and other data for the purposes described
    accept_button = None
    try:
        accept_button = driver.find_element(By.XPATH, "//button[@aria-label='Accept all']")
        # Press the button
        accept_button.click()
    except:
        pass
    try:
        accept_button = driver.find_element(By.XPATH, "//button[@aria-label='Accept the use of cookies and other data for the purposes described']")
        # Press the button
        accept_button.click()
    except:
        pass
    if accept_button == None:
        print("No accept button found")
        return None
    sleep(1)

    # Send the f key to the page to make the video fullscreen
    driver.find_element(By.TAG_NAME, "body").send_keys("f")
    sleep(3)


    return driver

def getVideoElement(driver):
    video = driver.find_element(By.TAG_NAME, "video")
    return video

def capture(video_element, filename="video.png"):
    video_element.screenshot(CAPTURE_DIR+filename)