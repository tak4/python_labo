import argparse
import shutil
import os
import sys

# chardet がインストールされているかチェック
try:
    import chardet
except ImportError:
    print("エラー: 'chardet' ライブラリがインストールされていません。")
    print("以下のコマンドを実行してインストールしてください:")
    print("pip install chardet")
    sys.exit(1)

def detect_encoding(file_path):
    """
    バイナリ読み込みによってファイルの文字コードを自動判定します。
    """
    with open(file_path, 'rb') as f:
        # 判定の精度と速度のバランスのため先頭10KBを読み込む
        raw_data = f.read(1024 * 10)
    
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = result['confidence']
    
    return encoding, confidence

def convert_file_encoding_auto(file_path, to_encoding='utf-8'):
    """
    変換元の文字コードを自動判定し、指定の文字コードへ変換します。
    変換前にバックアップ (.bak) を作成します。
    """
    if not os.path.exists(file_path):
        print(f"エラー: ファイルが見つかりません: {file_path}")
        return

    # --- 1. 文字コードの自動判定 ---
    from_encoding, confidence = detect_encoding(file_path)
    if not from_encoding:
        print(f"エラー: 文字コードを判定できませんでした: {file_path}")
        return
    
    print(f"自動判定結果: {from_encoding} (信頼度: {confidence:.2%})")

    # --- 2. バックアップの作成 ---
    backup_path = f"{file_path}.bak"
    try:
        shutil.copy2(file_path, backup_path)
        print(f"バックアップを作成しました: {backup_path}")

        # --- 3. 変換処理 ---
        # 判定されたエンコーディングで読み込み
        with open(file_path, 'r', encoding=from_encoding) as f:
            content = f.read()

        # 指定されたエンコーディングで上書き保存
        with open(file_path, 'w', encoding=to_encoding, newline='') as f:
            f.write(content)

        print(f"変換が完了しました: {file_path} ({from_encoding} -> {to_encoding})")

    except UnicodeDecodeError:
        print(f"エラー: 判定された文字コード '{from_encoding}' でファイルを正しく読み込めませんでした。")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="文字コードを自動判定して変換するスクリプト。")
    parser.add_argument("file", help="変換対象のファイルパス")
    parser.add_argument("-t", "--to-enc", default="utf-8", help="変換後の文字コード (デフォルト: utf-8)")

    args = parser.parse_args()
    convert_file_encoding_auto(args.file, args.to_enc)
