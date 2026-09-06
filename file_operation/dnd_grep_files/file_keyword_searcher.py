import os
import re
import sys
import yaml
from pathlib import Path
from base_keyword_searcher import BaseSearcher

class FileKeywordSearcher(BaseSearcher):
    """検索条件文字列(config.yaml)を元に指定ファイルを検索する
    """

    def __init__(self, paths: list):
        # 検索対象のパスを絶対パスに正規化する
        self.paths = [Path(p).resolve() for p in paths]

        # 設定ファイル読み込み
        if getattr(sys, "frozen", False):
            config_path = Path(sys.executable).parent / "config" / "config.yaml"
        else:
            config_path = Path(__file__).resolve().parent / "config" / "config.yaml"

        with open(config_path, 'r', encoding='utf-8') as yaml_file:
            self.data = yaml.safe_load(yaml_file)


    def execute(self, cancel_event=None, progress_callback=None):
        """ 検索を行う
        """
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
        print(target_path.parent)
        output_folder = target_path.parent / 'output'
        os.makedirs(output_folder, exist_ok=True)

        # 検索条件へアクセス
        search_conditions = self.data["search_conditions"]

        # 検索対象ファイル
        input_file = Path(target_path)
        # grep結果出力先ファイル名を取得
        output_file = output_folder / search_conditions["output_file"]

        # 検索条件の作成
        condition_list = []
        conditions = search_conditions["conditions"]
        for condition in conditions:
            name = condition["name"]
            search_word = condition["search_word"]

            # リテラル (メタ文字をエスケープする)
            parts = [re.escape(k) for k in search_word.get('literal',[])]

            # 正規表現
            parts = parts + [k for k in search_word.get('regex',[])]
            pattern = "|".join(parts)
            pattern = r"(" + pattern + r")"
            flags = re.MULTILINE
            regex = re.compile(pattern, flags)

            condition_list.append({'name': name, 'pattern': regex})

        try:
            with open(input_file, mode="r", encoding="utf-8", errors="ignore") as target_fp:
                with open(output_file, mode="w", encoding="utf-8") as output_fp:
                    for c in condition_list:
                        if cancel_event is not None and cancel_event.is_set():
                            break

                        output_fp.writelines(c['name'] + '\n')

                        # 進捗表示の為、行数を数える
                        target_fp.seek(0)
                        total_lines = sum(1 for _ in target_fp)
                        target_fp.seek(0)

                        for line_number, line in enumerate(target_fp, start=1):
                            if cancel_event is not None and cancel_event.is_set():
                                break

                            if progress_callback is not None:
                                progress_callback(
                                    f"検索中: {input_file.name}",
                                    line_number,
                                    total_lines,
                                )

                            # findall()を使用する
                            matches = c['pattern'].findall(line)
                            if matches:
                                for m in matches:
                                    output_fp.write(f"{line_number}: {line.rstrip(chr(10) + chr(13))}\n")
                            # # sub()を使用する
                            # m = regex.search(line)
                            # if m:
                            #     result = regex.sub(r'\g<1>', line)
                            #     print(i, result)

                        target_fp.seek(0)

        except OSError as e:
            print(f"{e}")
            raise
