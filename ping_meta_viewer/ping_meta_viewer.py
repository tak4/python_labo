from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS  # Exifタグ情報
import pprint

# 画像ファイルを読み込む
image = Image.open("./image/00201-2113766317.png")

# Exif 情報を取得
exif_info = image.getexif()

for k, v in exif_info.items():
    print(k, v)

exif = [TAGS.get(k, "Unknown") + f": {str(v)}" for k, v in exif_info.items()]
exif_str = "\n".join(exif)

print(exif_str)


# D:\develop\python\sd_viewer\image

# with open("./image/00201-2113766317.png", "rb") as bin:
with open("/mnt/d/develop/python/sd_viewer/image/00201-2113766317.png", "rb") as bin:
    # 最初の8バイトはPNGであることのシグネチャ（89 50 4E 47 0D 0A 1A 0A）
    signature = bin.read(8)
    print(signature)

    # チャンクの読み出し
    while True:
        # Length データのサイズ
        data_len_b = bin.read(4)
        data_len = int.from_bytes(data_len_b, "big")

        # Chunk Type チャンクの種類
        chunk_type_b = bin.read(4)
        chunk_type = chunk_type_b.decode()

        print(f"{chunk_type} : {data_len} byte")

        # Chunk Data データ
        data_b = bin.read(data_len)
        print(type(data_b))
        if chunk_type == "tEXt":
            data = data_b.decode()
            print(type(data))
            # print(data)
            # print(data.split("\0"))

        # CRC
        crc_b = bin.read(4)

        if chunk_type == "IEND":
            break