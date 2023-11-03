from PIL import Image

width = 40000000000000000000000000
height = 3000000000000000000000000

img  = Image.new( mode = "CMYK", size = (width, height), color = (209, 123, 193, 100) )
img.show()