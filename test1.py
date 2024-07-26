import requests
from PIL import Image
import os
import time

#DO NOT SHARE
TOKEN = "7361421105:ABHAYnvIqlRhMI_DKL2AWJ7tBc"
chat_id = "5579790010"
image_path = "apple.jpg"


image = Image.open(image_path)
width, height = image.size


os.makedirs('pixels', exist_ok=True)


def send_image(file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(file_path, 'rb') as image_file:
        response = requests.post(url, data={"chat_id": chat_id}, files={"photo": image_file})
    print(response.json())
    os.remove(file_path)


pixel_count = 0
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        pixel_image = Image.new("RGB", (1, 1), pixel)
        pixel_path = f"pixels/pixel_{x}_{y}.jpg"
        pixel_image.save(pixel_path)
        
        send_image(pixel_path)
        pixel_count += 1


        if pixel_count % 30 == 0:
            time.sleep(1)

print("All pixels sent and deleted successfully.")
