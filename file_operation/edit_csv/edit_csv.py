import argparse
import csv
import os

def update_csv_row(file_path, target_name, target_column, target_val):
    temp_file = file_path + '.tmp'
    updated = False

    with open(file_path, 'r', newline='', encoding='utf-8') as f_in, \
         open(temp_file, 'w', newline='', encoding='utf-8') as f_out:
        
        reader = csv.DictReader(f_in)
        writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
        
        writer.writeheader()
        for row in reader:
            if row['name'] == target_name:
                row[target_column] = target_val
                updated = True
            writer.writerow(row)

    if updated:
        os.replace(temp_file, file_path)
        print(f"Updated {target_name} successfully.")
    else:
        os.remove(temp_file)
        print(f"Name '{target_name}' not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="csvファイルを編集します")
    parser.add_argument("file", help="編集対象のcsvファイルパス")
    parser.add_argument("target_name", help="編集対象のデータ name")
    parser.add_argument("target_column", help="編集対象のデータ column")
    parser.add_argument("target_val", help="設定する値")

    args = parser.parse_args()

    print(args.file, args.target_name, args.target_column, args.target_val)
    
    update_csv_row(args.file, args.target_name, args.target_column, args.target_val)
