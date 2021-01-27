import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from PIL import (ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps,
                 ImageSequence)

import requests
from io import BytesIO

response = requests.get('https://scoresaber.com/imports/images/usr-avatars/76561198205370764.jpg')
img = Image.open(BytesIO(response.content))

image = img.convert("RGBA").resize((480, 480), 5)
response = requests.get('https://raw.githubusercontent.com/Daggy1234/dagpi-image/main/app/image/assets/communism.gif')
flag = Image.open(BytesIO(response.content))
image.putalpha(96)
frame_list = list()
for frame in ImageSequence.Iterator(flag):
    frame = frame.resize((480, 480), 5).convert("RGBA")
    frame.paste(image, (0, 0), image)
    frame_list.append(frame)
obj = BytesIO
frame_list[0].save("donk.gif", format='gif', save_all=True,
                    append_images=frame_list, loop=0, disposal=2,
                    optimize=True)
frame_list[0].save(obj, format='gif', save_all=True,
                    append_images=frame_list, loop=0, disposal=2,
                    optimize=True)
obj.seek(0)

