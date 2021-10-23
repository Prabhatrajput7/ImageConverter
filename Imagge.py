import sys
import os
from PIL import Image, ImageFilter

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)
for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{directory}{clean_name}.png', 'png')
    print('All Done!')