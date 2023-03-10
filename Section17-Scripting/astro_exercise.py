#
from PIL import Image, ImageFilter
try:
    astro_img = Image.open('images/astro.jpg')
    astro_img.size
except OSError as er:
    print('Error opening the file')
    raise er

# print(astro_img.size)
# Thumbnails keeps the same aspect ratio as opposed to resize
# The size is changed of the original one
astro_img.thumbnail((400, 400))
astro_img.show()
