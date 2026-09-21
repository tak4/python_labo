import os
import re
import sys
import yaml
from pathlib import Path
from executor.base.base_executor import BaseExecutor

class FileKeywordSearcher(BaseExecutor):
    """検索条件文字列(config.yaml)を元に指定ファイルを検索する
    """
    window_title = "Searcher"
    CHUNK_SIZE = 1024 * 1024

    def execute(self, paths: list, cancel_event=None, progress_callback=None):
        """ 検索を行う
        """
        # 検索対象のパスを絶対パスに正規化する
        self.paths = [Path(p).resolve() for p in paths]

        # 設定ファイル読み込み
        if getattr(sys, "frozen", False):
            config_path = Path(sys.executable).parent / "config" / "config.yaml"
        else:
            config_path = Path(__file__).resolve().parent / "config" / "config.yaml"

        with open(config_path, 'r', encoding='utf-8') as yaml_file:
            self.config_data = yaml.safe_load(yaml_file)


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

        # 検索条件へアクセス
        search_conditions = self.config_data["search_conditions"]

        # 検索対象ファイル
        input_file = Path(target_path)
        # grep結果出力先ファイル名を取得
        output_file = output_folder / search_conditions["output_file"]

        # 検索条件の作成
        compiled = []
        conditions = search_conditions["conditions"]
        for condition in conditions:
            name = condition["name"]
            search_word = condition["search_word"]

            # リテラル (メタ文字をエスケープする)
            parts = [
                re.escape(k)
                for k in search_word.get("literal", [])
                if k    # 空文字を除外
            ]

            # 正規表現
            parts += [
                k
                for k in search_word.get("regex", [])
                if k    # 空文字を除外
            ]

            # partsが空の場合はエラー
            if not parts:
                raise ValueError(f"検索条件が空です: {name}")

            pattern = "|".join(parts)
            pattern = r"(" + pattern + r")"
            try:
                compiled.append((name, re.compile(f"({pattern})")))
            except re.error as error:
                raise ValueError(
                    f"正規表現が不正です: {name}: {pattern}"
                ) from error

        try:
            with open(input_file, "rb", buffering=FileKeywordSearcher.CHUNK_SIZE) as source_fp:
                total_size = input_file.stat().st_size
                processed_size = 0

                with open(output_file, "w", encoding="utf-8") as output_fp:
                    search_results = {}

                    buffer = b""
                    line_number = 0

                    while True:
                        if cancel_event is not None and cancel_event.is_set():
                            break

                        chunk = source_fp.read(FileKeywordSearcher.CHUNK_SIZE)
                        if not chunk:
                            break

                        processed_size += len(chunk)
                        if progress_callback is not None and processed_size % (FileKeywordSearcher.CHUNK_SIZE * 10) == 0:
                            progress_callback(
                                f"検索中: {input_file.name}",
                                processed_size,
                                total_size,
                            )

                        buffer += chunk
                        lines = buffer.splitlines(keepends=True)

                        # 最後の行の末尾が改行ではない場合、1行が完結していない可能性があるので、
                        # linesからbufferに戻しておく
                        # 末尾改行であれば、1行完結しているので、bufferは空にしておく
                        if lines and not lines[-1].endswith(b"\n"):
                            buffer = lines.pop()
                        else:
                            buffer = b""

                        for raw_line in lines:
                            line_number += 1
                            line = raw_line.decode("utf-8", errors="ignore").rstrip("\r\n")

                            for name, regex in compiled:
                                if regex.search(line):
                                    search_results.setdefault(name, [])
                                    search_results[name].append((line_number, line))

                    # 端数の行が残っている場合
                    if buffer:
                        line_number += 1
                        line = buffer.decode("utf-8", errors="ignore").rstrip("\r\n")
                        for name, regex in compiled:
                            if regex.search(line):
                                search_results.setdefault(name, [])
                                search_results[name].append((line_number, line))

                    for ptn, match_list in search_results.items():
                        output_fp.write(ptn + "\n")
                        for m in match_list:
                            output_fp.write(f"{m[0]}: {m[1]}\n")


        except OSError as e:
            print(f"{e}")
            raise
