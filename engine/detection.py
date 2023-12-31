import cv2
from PIL import Image
import numpy as np
import requests
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

def preprocess_image(image_arr):

    # Convert to greyscale
    # grey = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(image_arr,(5,5),0)
    Image.fromarray(blur)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    # Dilate the image
    dilated = cv2.dilate(blur, kernel)
    Image.fromarray(dilated)

    # Close the image
    closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    Image.fromarray(closing)

    return closing


def preview_detection(output_image):
    plt.imshow(output_image)
    plt.show()

def save_detection(output_image, path):
    cv2.imwrite(path, output_image)


def count_individual_vehicles(image_path):
    im = cv2.imread(image_path)
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)

    # save_detection(output_image, "output/output.png")

    # Vehicle types to detect
    vehicles = ['car', 'truck', 'bus']

    # Return each type of vehicle count individually
    return {v: label.count(v) for v in vehicles}





def count_total_vehicles(image_path):
    v = count_individual_vehicles(image_path)
    print(v)

    return sum(v.values())
