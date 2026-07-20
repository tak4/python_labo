

class FileKeywordSearcher():
    """
    """

    def __init__(self, paths: list):
        # 検索対象のパス
        self.paths = paths

    def search(self):
        """ 
        """
        # Drag and Drop で取得したディレクトリを順に処理する
        for p in self.paths:
            self._grep_path(p)


    def _grep_path(self, target_path: str):
        """ 
        """

        # grep結果出力先ディレクトリを作成する
        output_folder = os.path.join(target_path, 'output')
        os.makedirs(output_folder, exist_ok=True)

        target_files = {}
        p = Path(target_path)
        target_files = [str(p) for p in p.rglob('*.log')]

        # ダブルクォーテーションで囲まれた文字列を抜き出す
        pattern = r'.*"([^\"]+)".*'
        regex = re.compile(pattern)

        for target_file in target_files:
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


