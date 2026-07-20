import io
import zipfile

with zipfile.ZipFile("sample_data.zip", "r") as z:
    # ZIP内の全ファイル・フォルダ名を表示
    namelist = z.namelist()
    print(namelist)

with zipfile.ZipFile("sample_data.zip", "r") as z:
    for name in z.namelist():
        print(name)

    target_name = "test1.txt"
    candidates = [name for name in z.namelist() if name == target_name or name.endswith("/" + target_name)]
    if not candidates:
        raise FileNotFoundError(f"There is no item named {target_name!r} in the archive")

    with z.open(candidates[0]) as f:
        # バイトストリームをテキストストリームに変換
        with io.TextIOWrapper(f, encoding="utf-8") as text_file:
            for line in text_file:
                print(line.strip())