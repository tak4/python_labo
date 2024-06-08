from PIL import Image
import os
import sys

# ファイル名取得
args = sys.argv
if 1 == len(args):
    print("Usage " + args[0] + " jpeg folder")
    sys.exit()

# 圧縮したい画像が保存されているフォルダパスを指定
file_path = args[1]
print(file_path)

# 圧縮後の画像を保存したいフォルダパスを指定
save_file_path = os.path.join(file_path, 'output')
os.makedirs(save_file_path, exist_ok=True)

# os.makedirs(save_file_path)
print(save_file_path)

#######ユーザー入力変数#######

# 保存したい画像フォーマットを指定
# jpg, png, webpのいずれかを指定する
# 圧縮したい画像がjpg画像の場合の保存フォーマット
save_format_jpg = "jpg"

# 圧縮したい画像がpng画像の場合の保存フォーマット
save_format_png = "png"

# 圧縮したい画像がwebp画像の場合の保存フォーマット
save_format_webp = "webp"

# 保存したい画像のファイル名の接尾語を指定
save_filename_suffix = "_comp"

# 「jpg」と「webp」画像の圧縮率の指定
# 「jpg」の場合は、0-95, 「webp」の場合は、0-100で指定
compression_rate_jpg = 50
compression_rate_webp = 50

# 「png」画像の色数の指定
# 1 - 256で指定
compression_color_num = 256

##########プロセス処理部分##########

# フォルダの区切り文字を取得(windowとmacで異なるため)
Delimiter_path = os.sep

# 圧縮したい画像のファイル名取得
filename_pic_list = os.listdir(file_path)

# for文により、フォルダ内のファイルの数だけ、下記のコードを実行
for filename_pic in filename_pic_list:

    print(filename_pic)

    # 元の画像ファイル名をファイル名と拡張子に分割する。
    file, ext = os.path.splitext(filename_pic)

    # 画像フォーマットによる場合わけ
    if ext == '.png':
        # 圧縮したい画像の読み込み。
        img = Image.open(file_path + Delimiter_path + filename_pic)
        # 画像の色数を削減
        img = img.convert("P", palette=Image.ADAPTIVE,
                          colors=compression_color_num)
        # 画像を指定した色数で保存(pngの場合)
        img.save((save_file_path + Delimiter_path + file +
                 save_filename_suffix + '.' + save_format_png), optimize=True)

    elif ext == '.jpg' or ext == '.JPG' or ext == '.webp':
        # 圧縮したい画像の読み込み。
        img = Image.open(file_path + Delimiter_path + filename_pic)

        # 保存する画像フォーマットを拡張子により、指定
        if ext == '.jpg' or ext == '.JPG':
            save_format = save_format_jpg
            compression_rate = compression_rate_jpg
        elif ext == '.webp':
            save_format = save_format_webp
            compression_rate = compression_rate_webp

        # 画像を指定した圧縮率で保存(jpgとwebpの場合)
        img.save((save_file_path + Delimiter_path + file + save_filename_suffix +
                 "." + save_format), optimize=True, quality=compression_rate)