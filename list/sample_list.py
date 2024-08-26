import numpy as np

float_list = [ round(x * 0.0001, 4) for x in range(0, 4096, 1)]

width = 64
height = 64
hlength = 4096

buf = {'I': [{'hm': None}] }
buf['I'][0]['hm'] = float_list

# 内包表記
with open('output.csv', 'w') as f:
    print(*[",".join(
        [str(__buf_data) for __buf_data in buf['I'][0]['hm']][__start_num:(__start_num+width)]) 
        for __start_num in range(0, hlength-1, width)],
        sep="\n", 
        file=f
    )

# 内包表記をforに分解
with open('output_for_loop.csv', 'w') as f:
    for __start_num in range(0, hlength-1, width):
        # 全要素について float から str へ変換
        l_str_4096 = [str(__buf_data) for __buf_data in buf['I'][0]['hm']]
        # 64要素づつ切り出してリスト化
        l_str_64 = l_str_4096[__start_num:(__start_num+width)]
        # 64要素づつ切り出したリスト要素を , で接続
        l_str_64_comma_sep = ",".join(l_str_64)
        # 64要素づつファイル出力
        print(l_str_64_comma_sep, file=f)

