import sys
import yaml
from pathlib import Path
from pydlt import DltFileReader, DltFileWriter

from executor.base.base_executor import BaseExecutor

class DltMerger(BaseExecutor):
    def execute(self, paths: list, cancel_event=None, progress_callback=None):

        # 検索対象のパスを絶対パスに正規化する
        self.paths = [Path(p).resolve() for p in paths]

        # 設定ファイル読み込み
        if getattr(sys, "frozen", False):
            config_path = Path(sys.executable).parent / "config" / "config.yaml"
        else:
            config_path = Path(__file__).resolve().parent / "config" / "config.yaml"

        with open(config_path, 'r', encoding='utf-8') as yaml_file:
            self.config_data = yaml.safe_load(yaml_file)

        merged_dlt = self.config_data['merged_dlt']
        merged_txt = self.config_data['merged_txt']

        # Drag and Drop で取得したファイルをリスト化する
        files_list = []
        for path in self.paths:
            if cancel_event is not None and cancel_event.is_set():
                break

            if not path.exists():
                raise FileNotFoundError(f"検索対象が存在しません: {path}")

            if path.is_file():
                if path.name == merged_dlt:
                    continue
                files_list.append(path)
            elif path.is_dir():
                for p in path.glob("*.dlt"):
                    # シンボリックリンクは除外
                    if not p.is_file() or p.is_symlink():
                        continue
                    # マージ済みファイルは除外
                    if p.name == merged_dlt:
                        continue
                    files_list.append(p)
            else:
                pass

        input_files = sorted(
            f for f in files_list
        )

        output_file_dlt = input_files[0].parent / merged_dlt
        output_file_txt = input_files[0].parent / merged_txt
        # print(output_file_dlt)
        # print()
        # for i in input_files:
        #     print(i)

        with open(output_file_txt, "w") as text_writer:
            with DltFileWriter(str(output_file_dlt)) as writer:
                total_fileno = len(input_files)
                for fileno, input_file in enumerate(input_files, start=1):
                    print(f"marging: {input_file.name}")

                    if cancel_event is not None and cancel_event.is_set():
                        break

                    if progress_callback is not None:
                        progress_callback(
                            f"marging: {input_file.name}",
                            fileno,
                            total_fileno,
                        )

                    reader = DltFileReader(str(input_file))

                    for message in reader:
                        writer.write_messages([message])
                        text_writer.write(str(message) + "\n")

        print("complete")
