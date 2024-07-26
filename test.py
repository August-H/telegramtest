import requests
from PIL import Image
import os

#DO NOT SHARE
TOKEN = "7361421105:ABHAYNcu0CMQVtH3ng"
chat_id = "5579790010"
image_path = "apple.jpg"


image = Image.open(image_path)
width, height = image.size


half_width = width // 2
half_height = height // 2


quadrants = [
    image.crop((0, 0, half_width, half_height)),
    image.crop((half_width, 0, width, half_height)),
    image.crop((0, half_height, half_width, height)),
    image.crop((half_width, half_height, width, height))
]


quadrant_paths = []
for i, quadrant in enumerate(quadrants):
    quadrant_path = f"imageparse/quadrant_{i + 1}.jpg"
    quadrant.save(quadrant_path)
    quadrant_paths.append(quadrant_path)


url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
for quadrant_path in quadrant_paths:
    with open(quadrant_path, 'rb') as image_file:
        response = requests.post(url, data={"chat_id": chat_id}, files={"photo": image_file})
        print(response.json())

    os.remove(quadrant_path)


