from engine.detection import count_total_cars


# Replace 'image_path' with the path to your road traffic image
total_cars = count_total_cars('captures/video0.png')


print('Number of cars in the image is '+ str(total_cars))