from engine.detection import count_total_vehicles


# Replace 'image_path' with the path to your road traffic image
total_cars = count_total_vehicles('captures/capture_1690435284.638245.png')


print('Number of cars in the image is '+ str(total_cars))