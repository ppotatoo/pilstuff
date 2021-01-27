import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

import requests
from io import BytesIO

response = requests.get('https://th.bing.com/th/id/R459510f67944502502bbbff50f5ca59a?rik=e%2bp7D2U%2b%2bgGvLQ&riu=http%3a%2f%2fwww.timvandevall.com%2fwp-content%2fuploads%2fWanted-Poster-Template.jpg&ehk=wekoA0bgqQfOUtTBR71KOr1HjIUS2HNDlUauvPinyM0%3d&risl=&pid=ImgRaw')
img = Image.open(BytesIO(response.content))

response = requests.get('https://scoresaber.com/imports/images/usr-avatars/76561198205370764.jpg')

img2 = Image.open(BytesIO(response.content))
img2 = img2.resize((540, 540))

img.paste(img2, (170, 419))

#540

img.show()