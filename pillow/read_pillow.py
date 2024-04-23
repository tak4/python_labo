import numpy as np
from PIL import Image

im = Image.open("./img/R.bmp")

array = np.array(im)

np.set_printoptions(threshold=32*32*3)
print(array)
print(np.shape(array))

np.savetxt('./output/np_save_bmp_R.csv', array, delimiter=',', fmt='%x')


im = Image.open("./img/R_red.bmp")

array = np.array(im)

np.set_printoptions(threshold=32*32*3)
print(array)
print(np.shape(array))

np.savetxt('./output/np_save_bmp_R_red.csv', array, delimiter=',', fmt='%x')