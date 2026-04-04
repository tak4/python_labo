import argparse
import shutil
import os

def convert_file_encoding(file_path, from_encoding='shift_jis', to_encoding='utf-8'):
    """
    標準ライブラリのみを使用し、指定された文字コード間で変換を行います。
    """
    if not os.path.exists(file_path):
        print(f"エラー: ファイルが見つかりません: {file_path}")
        return

    # バックアップファイル名 (.bak)
    backup_path = f"{file_path}.bak"

    try:
        # --- バックアップ処理 ---
        shutil.copy2(file_path, backup_path)
        print(f"バックアップを作成しました: {backup_path}")

        # --- 読み込みと変換 ---
        # 変換元(from_encoding)を明示して読み込む
        with open(file_path, 'r', encoding=from_encoding) as f:
            content = f.read()

        # 変換先(to_encoding)で上書き保存
        with open(file_path, 'w', encoding=to_encoding, newline='') as f:
            f.write(content)

        print(f"変換が完了しました: {file_path} ({from_encoding} -> {to_encoding})")

    except UnicodeDecodeError:
        print(f"エラー: 指定された文字コード '{from_encoding}' でファイルを読み込めませんでした。")
        print(f"実際の文字コードが異なる可能性があります。'-f' オプションで正しい文字コードを指定してください。")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="テキストファイルの文字コードを変換します (標準ライブラリのみ使用)。")
    parser.add_argument("file", help="変換対象のファイルパス")
    parser.add_argument("-f", "--from-enc", default="shift_jis", help="変換元の文字コード (デフォルト: shift_jis)")
    parser.add_argument("-t", "--to-enc", default="utf-8", help="変換後の文字コード (デフォルト: utf-8)")

    args = parser.parse_args()
    convert_file_encoding(args.file, args.from_enc, args.to_enc)
