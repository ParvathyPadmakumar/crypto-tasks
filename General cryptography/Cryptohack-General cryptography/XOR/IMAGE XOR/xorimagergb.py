from PIL import Image, ImageChops
im1 = Image.open('lemur.png',"r")
im2 = Image.open('flag.png',"r")

im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
im3.show()
