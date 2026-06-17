import argparse
import csv
from difflib import SequenceMatcher
from openpyxl import Workbook

parser = argparse.ArgumentParser(description="Sample CLI")
parser.add_argument("--input_list", type=str, default="input_list.txt", help="input list")
parser.add_argument("--target_list", type=str, default="target_list.txt", help="target list")
parser.add_argument("--output_csv", type=str, default="result.csv", help="output csv")
parser.add_argument("--output_xlsx", type=str, default="result.xlsx", help="output xlsx")
parser.add_argument("--verbose", action="store_true", help="Verbose mode")

args = parser.parse_args()

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Excel ワークブックの作成
wb = Workbook()
ws = wb.active
ws.title = "Similarity Results"

with open(args.output_csv, 'w', newline='') as csvfile:
    result_writer = csv.writer(csvfile)
    with open(args.input_list, mode="r", encoding="utf-8") as input_f:
        while True:
            input_f_line = input_f.readline()
            with open(args.target_list, mode="r", encoding="utf-8") as target_f:
                while True:
                    target_f_line = target_f.readline()
                    if not target_f_line:          # ファイルの終端に達したら終了
                        break                    
                    check_line = input_f_line.rstrip()
                    target_line = target_f_line.rstrip()
                    sim_score = similarity(input_f_line, target_f_line)
                    
                    # CSV に書き込み
                    result_writer.writerow([check_line, target_line, sim_score])
                    
                    # Excel に書き込み
                    ws.append([check_line, target_line, sim_score])
            if not input_f_line:          # ファイルの終端に達したら終了
                break

# Excel ファイルを保存
if args.output_xlsx:
    wb.save(args.output_xlsx)

