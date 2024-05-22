import numpy as np
from PIL import Image

#
# 画像入力
#
im = Image.open("./img/R.bmp")
print(type(im))

# imageをndarrayに変換
np_array = np.array(im, dtype=np.int32)

# print での 表示要素数を設定 32pixel x 32pixel
np.set_printoptions(threshold=32*32)

print(np.shape(np_array))
print(np_array)

# CSV形式でファイル保存
np.savetxt('./output/np_save_bmp_R.csv', np_array, delimiter=',', fmt='%x')

# reshape
print()
reshape_np_array = np.reshape(np_array, (32,32))
print(np.shape(reshape_np_array))
print(reshape_np_array)

#
# 画像出力
#
# NumPy配列を画像に変換
array = np_array * 255
image = Image.fromarray(array)

# 画像をRGBカラーモードに変換
image_RGB = image.convert("RGB")
# 画像ファイル出力
image_RGB.save("./output/R_bmp_RGB.bmp")

# 画像をグレースケールに変換
image_L = image.convert("L")
# 画像ファイル出力
image_L.save("./output/R_bmp_L.bmp")

# rot90 ※copy()でdeep copyとなる
print()
rot90_np_array = np.rot90(np_array).copy()
print(np.shape(rot90_np_array))
print(rot90_np_array)

#
# 画像出力
#
# NumPy配列を画像に変換
array = rot90_np_array * 255
image = Image.fromarray(array)

# 画像をRGBカラーモードに変換
image_RGB = image.convert("RGB")
# 画像ファイル出力
image_RGB.save("./output/R_bmp_RGB_rot90.bmp")

# 画像をグレースケールに変換
image_L = image.convert("L")
# 画像ファイル出力
image_L.save("./output/R_bmp_L_rot90.bmp")



# #
# # 画像入力
# #
# im_red = Image.open("./img/R_red.bmp")
# print(type(im_red))

# # imageをndarrayに変換
# np_array = np.array(im_red, dtype=np.int32)

# # print での 表示要素数を設定 32pixel x 32pixel x RGB
# np.set_printoptions(threshold=32*32*3)

# print(np.shape(np_array))
# print(np_array)

# # NumPy配列を画像に変換
# image = Image.fromarray(array)

# #
# # 画像出力
# #
# # 画像をRGBカラーモードに変換
# image_red_RGB = image.convert("RGB")
# # 画像ファイル出力
# image_RGB.save("./output/R_red_bmp_RGB.bmp")


# im = Image.open("./img/R_red.bmp")
# im.convert("RGB")

# pixelSizeTuple = im.size

# plist = []

# for i in range(pixelSizeTuple[0]):
# 	for j in range(pixelSizeTuple[1]):
# 		p = im.getpixel((i,j))
# 		plist.append(p)
		
# print(plist)
