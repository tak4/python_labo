import numpy as np
from PIL import Image

im = Image.open("./img/R.bmp")

array = np.array(im, dtype=np.int32)

np.set_printoptions(threshold=32*32*3)
print(np.shape(array), type(im))
print(array)

np.savetxt('./output/np_save_bmp_R.csv', array, delimiter=',', fmt='%x')


im = Image.open("./img/R_red.bmp")

array = np.array(im, dtype=np.int32)

np.set_printoptions(threshold=32*32*3)
print(np.shape(array), type(im))
print(array)

im = Image.open("./img/R_red.bmp")
im.convert("RGB")

pixelSizeTuple = im.size

plist = []

for i in range(pixelSizeTuple[0]):
	for j in range(pixelSizeTuple[1]):
		p = im.getpixel((i,j))
		plist.append(p)
		
print(plist)
