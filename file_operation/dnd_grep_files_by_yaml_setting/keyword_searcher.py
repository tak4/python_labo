import re
import yaml
from pathlib import Path
from pathlib import PurePosixPath
from base_keyword_searcher import BaseSearcher

class KeywordSearcher(BaseSearcher):
    """検索条件文字列(config.yaml)を元に指定フォルダ内を検索する
    """

    def __init__(self, paths: list):
        # 検索対象のパスを絶対パスに正規化する
        self.paths = [Path(p).resolve() for p in paths]

        # 設定ファイル読み込み
        config_path = Path(__file__).parent / 'config' / 'config.yaml'
        with open(config_path, 'r', encoding='utf-8') as yaml_file:
            self.data = yaml.safe_load(yaml_file)


    def execute(self, cancel_event=None, progress_callback=None):
        """ 検索を行う
        """
        # Drag and Drop で取得したディレクトリを順に処理する
        for p in self.paths:
            if cancel_event is not None and cancel_event.is_set():
                break
            self._grep_path(p, cancel_event, progress_callback)


    def _natural_path_key(self, path):
        """ 検索結果ソート用の為のキー関数
        """
        key = []
        # as_posix()でパス区切り文字を/に統一する
        # OS異存の実ファイルパスではなく、文字列としてのパス表現で扱いたい為、
        # PurePosixPath を使用する
        for part in PurePosixPath(path.as_posix()).parts:
            m = re.search(r'(?i)(N)(\d+)', part)
            if m:
                prefix, number = m.groups()
                key.append((prefix or "", int(number), part.lower()))
            else:
                key.append(("", 0, part.lower()))
        return tuple(key)


    def _grep_path(self, target_path: Path, cancel_event=None, progress_callback=None):
        """ 指定パス内の検索を行う
        """

        # grep結果出力先ディレクトリを作成する
        output_folder = target_path.joinpath("output")
        output_folder.mkdir(exist_ok=True)

        # 検索条件(condition)ごとの処理
        for condition in self.data["search_conditions"]:
            if cancel_event is not None and cancel_event.is_set():
                break

            # 検索対象ファイル名を取得する
            files = self._get_rglob_file_list(target_path, condition["target_file"], output_folder)

            # grep結果出力先ファイル名を取得
            output_file = output_folder / condition["output_file"]

            # grep実行
            self._do_regex_search(target_path, 
                                  files, 
                                  output_file, 
                                  condition["keywords"], 
                                  cancel_event, 
                                  progress_callback)


    def _get_rglob_file_list(self, path: Path, 
                             target_files: list[str], 
                             excluded_dir: Path | None = None) -> list[Path]:
        """ 検索対象ファイルをパス名＋ファイル名で取得する
        """

        # rglobでフルパス取得する 相対パスを得る処理の為、Pathオブジェクトで保持しておく
        target_file_list = []
        for target_file in target_files:
            for file_path in path.rglob(target_file):
                if excluded_dir is not None and excluded_dir in file_path.parents:
                    continue
                target_file_list.append(file_path)

        return target_file_list


    def _do_regex_search(self, target_path: Path, 
                         target_files_with_path: list[Path], 
                         output_file: str, 
                         keywords: dict, 
                         cancel_event=None, 
                         progress_callback=None):
        """ リテラル／正規表現による検索を行う
        """

        # 検索条件の作成
        # リテラル (メタ文字をエスケープする)
        parts = [re.escape(k) for k in keywords.get('literal',[])]
        # 正規表現
        parts = parts + [k for k in keywords.get('regex',[])]

        pattern = "|".join(parts)
        pattern = r"(" + pattern + r")"
        flags = re.MULTILINE
        regex = re.compile(pattern, flags)

        # 相対パスにする為に、検索対象のパスを用意しておく
        base = Path(target_path).resolve()

        # 検索の実行
        # 結果をoutput_fileに出力する
        records = []
        total_files = len(target_files_with_path)
        try:
            with open(output_file, mode='w', encoding="utf-8", errors="ignore") as o_fp:    # 結果出力ファイル
                for index, target_file in enumerate(target_files_with_path, start=1):
                    if cancel_event is not None and cancel_event.is_set():
                        break

                    if progress_callback is not None:
                        progress_callback(f"検索中: {target_file.name}", index, total_files)

                    with open(target_file, mode='r', encoding="utf-8", errors="ignore") as i_fp:    # 検索対象ファイル
                        for i, line in enumerate(i_fp, start=1):
                            if regex.search(line):
                                # 検索結果のファイル名は相対パスにする
                                relative_path = target_file.relative_to(base)
                                # 検索結果をソートする為に一旦結果をリストで保持
                                records.append((relative_path, i, line.rstrip()))
                                
                for relative_path, i, line in sorted(records, key=lambda x: self._natural_path_key(x[0])):
                    o_fp.write(f"{relative_path}:{i}:{line}\n")

        except OSError as e:
            print(f"{e}")


