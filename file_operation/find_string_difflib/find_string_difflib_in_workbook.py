from difflib import SequenceMatcher
import openpyxl


wb = openpyxl.load_workbook("check_target.xlsx") # Excelファイルの読み込み

sheet_names = wb.sheetnames # シート名一覧取得

ws_target = wb['target'] # シートの取得
ws_list = wb['list'] # シートの取得

row_target = 1
while True:
    value_target = ws_target.cell(row=row_target, column=1).value
    if value_target == None:
        break

    row_list = 1
    while True:
        value_list = ws_list.cell(row=row_list, column=1).value
        if value_list == None:
            break

        print(value_list)
        row_list += 1

    print(value_target)
    row_target += 1
