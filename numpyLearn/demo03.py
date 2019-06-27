import numpy as np
from PIL import Image

img=Image.open('img.png')
print(img,type(img))

im=np.array(img)
print(type(im),im.dtype)
im =[255,255,255,255*2]-im
print(type(im),im.dtype)
im=im.astype(np.uint8)
newImage=Image.fromarray(im)
newImage.save('2.png')