# docomo スケジュール アプリ のエクスポートデータ 拡張子 vcs を
# Outlookでインポートした時に文字化けしないように、UTF-8 -> SJIS 変換を行う
# vscファイルは、SUMMARY で始まる行に、文字コード種別と文字列データが記述されており、
# 文字コード種別と文字列データの両方をSJISにする必要がある。
# 尚、文字列データは、Quoted-Printableエンコードされている為、
# quopriモジュールでデコードしてからSJIS変換を行う。

import quopri
import re
import sys

import chardet

if len(sys.argv) < 2:
    print("使用方法: python vcs_change_encode.py <input_file>")
    sys.exit(1)

RE_SUMMARY = re.compile(r"SUMMARY;CHARSET=(.+);ENCODING=QUOTED-PRINTABLE:(=.+)")

input_file = sys.argv[1]
output_file = "out_" + input_file

with open(output_file, 'w', encoding='UTF-8') as fo:
    with open(input_file, 'r', encoding='UTF-8') as fi:
        lines = fi.readlines()
        for line in lines:
            m = RE_SUMMARY.match(line)
            if m:
                if m.group(1) == "UTF-8":
                    qp_encoded = m.group(2)

                    # Quoted-Printableデコード（バイト列として取得）
                    utf8_bytes = quopri.decodestring(qp_encoded)

                    try:
                        # UTF-8デコード -> Unicode文字列
                        text = utf8_bytes.decode("utf-8")
  
                        # Shift_JISエンコード -> Quoted-Printableエンコード
                        sjis_bytes = text.encode("shift_jis")                        
                        sjis_qp = quopri.encodestring(sjis_bytes).decode("ascii").upper()
                        print(sjis_qp)

                    except UnicodeDecodeError as e:
                        print(e)
                        result = chardet.detect(utf8_bytes)
                        print(result)

                    # 出力行を組み立て
                    line = f"SUMMARY;CHARSET=SHIFT_JIS;ENCODING=QUOTED-PRINTABLE:{sjis_qp}\n"

            fo.write(line)

