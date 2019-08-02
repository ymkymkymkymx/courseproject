from PIL import Image
from PIL import ImageOps
import PIL
import numpy
im = Image.open("shirt.PNG")
newim=PIL.ImageOps.fit(im, (28,28), method=0, bleed=0.0, centering=(0.5, 0.5))
newim=PIL.ImageOps.grayscale(newim)
newim=PIL.ImageOps.invert(newim)
newim.save("newshirt.PNG")