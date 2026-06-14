import csv
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

with open('result.csv', 'w', newline='') as csvfile:
    result_writer = csv.writer(csvfile)
    with open("input.txt", mode="r", encoding="utf-8") as input_f:
        while True:
            input_f_line = input_f.readline()
            with open("target.txt", mode="r", encoding="utf-8") as target_f:
                while True:
                    target_f_line = target_f.readline()
                    if not target_f_line:          # ファイルの終端に達したら終了
                        break                    
                    result_writer.writerow([input_f_line.rstrip(), target_f_line.rstrip(), similarity(input_f_line, target_f_line)])
            if not input_f_line:          # ファイルの終端に達したら終了
                break

