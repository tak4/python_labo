import numpy as np
from PIL import Image

# data = [round(i * 0.01, 2) for i in range(100*100)]
# print(data)

# 3x3のNumPy配列を作成
array = np.array([
    [100., 150., 200.],
    [50., 100., 150.],
    [0., 50., 100.]
])

# array = np.array([
#     [255., 0., 0.],
#     [255., 0., 0.],
#     [255., 0., 0.]
# ])

# NumPy配列を画像に変換
image = Image.fromarray(array)

# 画像をRGBカラーモードに変換
image = image.convert("L")

# 画像を保存
image.save("./output/3x3_image.bmp")
