import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from PIL import (ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps,
                 ImageSequence)

import requests
from io import BytesIO
import random

response = requests.get('https://scoresaber.com/imports/images/usr-avatars/76561198205370764.jpg')
im = Image.open(BytesIO(response.content))
im = im.resize((500, 500), 1)
response = requests.get('https://raw.githubusercontent.com/Daggy1234/dagpi-image/main/app/image/assets/triggered.png')
overlay = Image.open(BytesIO(response.content))
ml = []
for i in range(0, 30):
    blank = Image.new("RGBA", (400, 400))
    x = -1 * (random.randint(50, 100))
    y = -1 * (random.randint(50, 100))
    blank.paste(im, (x, y))
    rm = Image.new("RGBA", (400, 400), color=(255, 0, 0, 80))
    blank.paste(rm, mask=rm)
    blank.paste(overlay, mask=overlay)
    ml.append(blank)

obj = BytesIO
frames = ml
frames[0].save("triggered.gif", format='gif', save_all=True,
                    append_images=frames, loop=0, disposal=2,
                    optimize=True)
frames[0].save(obj, format='gif', save_all=True,
                    append_images=frames, loop=0, disposal=2,
                    optimize=True)
obj.seek(0)

