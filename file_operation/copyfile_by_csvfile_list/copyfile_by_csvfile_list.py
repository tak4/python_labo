import csv
import os
import shutil


def main():
    with open('./copyfile_list_rusult.txt', 'w') as output_file:
        with open('./copyfile_list.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                source_file = os.path.join(row['source_path'], row['source_file'])
                # 空文字／空白のみなら source_file 名を使う
                target_basename = row.get('target_file', '').strip() or row['source_file']
                target_file = os.path.join(
                    row['target_path'], 
                    target_basename
                )
                output_file.write('{}\t{}\n'.format(source_file, target_file))
                shutil.copy2(source_file, target_file)

if __name__ == "__main__":
    main()
