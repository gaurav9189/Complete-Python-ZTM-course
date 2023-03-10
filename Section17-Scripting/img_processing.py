from PIL import Image, ImageFilter
img = Image.open('images/pikachu.jpg')

print(img.format)
print(img.size)
print(img.mode)
print(dir(img))

im = img.convert('L')
im.save(fp='images/pika_black.png', format='png')
im.show()

# Filter methods on Python image Lib
ims = img.filter(ImageFilter.SMOOTH)
ims.show()

# resizing of images
img_bulba = Image.open('images/bulbasaur.jpg')
img_bulba_size = img_bulba.resize(size=(200, 200))
img_bulba_size.show()

# cropping images
box = (100, 100, 500, 500)
box_bula = img_bulba_size.crop(box=box)
box_bula.show()
