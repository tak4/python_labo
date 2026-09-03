import os
import re
import os
from pathlib import Path

class FileKeywordSearcher():
    """
    """

    def __init__(self, files: list):
        # 検索対象のファイル
        self.files = files

    def search(self):
        """ 
        """
        # Drag and Drop で取得したファイルを順に処理する
        for p in self.files:
            if Path(p).is_file():
                self._grep_files(p)
            else:
                pass


    def _grep_files(self, target_file: str):
        """ 
        """
        print(target_file)
        path = Path(target_file)

        # grep結果出力先ディレクトリを作成する
        output_folder = os.path.join(path.parent, 'output')
        os.makedirs(output_folder, exist_ok=True)

        # ダブルクォーテーションで囲まれた文字列を抜き出す
        pattern = r'.*"([^\"]+)".*'
        regex = re.compile(pattern)

        with open(target_file, mode='r', encoding="utf-8", errors="ignore") as target_fp:
            for i, line in enumerate(target_fp, start=1):
                # findall()を使用する
                matches = regex.findall(line)
                if matches:
                    for m in matches:
                        print(i, m)
                # sub()を使用する
                m = regex.search(line)
                if m:
                    result = regex.sub(r'\g<1>', line)
                    print(i, result)


