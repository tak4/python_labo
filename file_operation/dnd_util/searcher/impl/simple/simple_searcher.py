import os
import re
from pathlib import Path
from searcher.base.base_searcher import BaseSearcher

class SimpleSearcher(BaseSearcher):
    """
    """

    def execute(self, paths: list, cancel_event=None, progress_callback=None):
        """ 検索を行う
        """
        # 検索対象のパスを絶対パスに正規化する
        self.paths = [Path(p).resolve() for p in paths]

        # Drag and Drop で取得したファイルを順に処理する
        for path in self.paths:
            if cancel_event is not None and cancel_event.is_set():
                break

            if not path.exists():
                raise FileNotFoundError(f"検索対象が存在しません: {path}")

            if not path.is_file():
                raise IsADirectoryError(f"ファイルではありません: {path}")

            self._grep_path(path, cancel_event, progress_callback)


    def _grep_path(self, target_path: Path, cancel_event=None, progress_callback=None):
        """指定ファイルの検索を行う
        """
        # grep結果出力先ディレクトリを作成する
        output_folder = target_path.parent / 'output'
        os.makedirs(output_folder, exist_ok=True)

        # 検索対象ファイル
        input_file = Path(target_path)
        # grep結果出力先ファイル名を取得
        output_file = output_folder / 'grep_result.txt'

        # ダブルクォーテーションで囲まれた文字列を抜き出す
        pattern = r'.*"([^\"]+)".*'
        regex = re.compile(pattern)

        try:
            with open(input_file, mode="r", encoding="utf-8", errors="ignore") as target_fp:
                with open(output_file, mode="w", encoding="utf-8") as output_fp:

                    # 進捗表示の為、行数を数える
                    target_fp.seek(0)
                    total_lines = sum(1 for _ in target_fp)
                    target_fp.seek(0)

                    for line_number, line in enumerate(target_fp, start=1):

                        if progress_callback is not None:
                            progress_callback(
                                f"検索中: {input_file.name}",
                                line_number,
                                total_lines,
                            )

                        # findall()を使用する
                        matches = regex.findall(line)
                        if matches:
                            output_fp.writelines(f'{line_number}, {m}')
                        # sub()を使用する
                        m = regex.search(line)
                        if m:
                            result = regex.sub(r'\g<1>', line)
                            output_fp.writelines(f'{line_number}, {result}')

        except OSError as e:
            print(f"{e}")
            raise
