import sys
import os
from PIL import Image, ImageFilter

in_dir = sys.argv[1]
out_dir = sys.argv[2]
abs_path = '/Users/deepaliyadav/Documents/VScode/Udemy-python/Section17-Scripting'
files = os.listdir(f'{abs_path}/images')
images = []

try:
    if not os.path.exists(f'{abs_path}/{out_dir}'):
        os.mkdir(f'{abs_path}/{out_dir}')
        print(f'Your o/p directory {out_dir} is now made')

    else:
        print('Something didn\'nt go right or it already exists')
except OSError as er:
    print('OS issue?')


for i in files:
    images.append((os.path.splitext(i)))
jpg = [name for name, extn in images if extn == '.jpg']

try:
    for i in jpg:
        im = Image.open(f'images/{i}.jpg')
        print(f'Saving {i} as png now')
        im.save(f'{out_dir}/{i}.png', 'png')

except OSError:
    print('Cannot convert the file')
