import shutil

def convert_file_encoding(file_path, from_encoding='shift_jis', to_encoding='utf-8'):
    try:
        # 変換前にバックアップを作成 (.bakを付与)
        backup_path = f"{file_path}.bak"
        shutil.copy2(file_path, backup_path)

        # ファイルをメモリに読み込む
        with open(file_path, 'r', encoding=from_encoding) as f:
            content = f.read()

        # 同じファイルパスで上書き保存
        with open(file_path, 'w', encoding=to_encoding, newline='') as f:
            f.write(content)

        print(f"変換完了: {file_path} (Backup: {backup_path})")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# 使用例
convert_file_encoding('sample.txt', 'shift_jis', 'utf-8')

