import openpyxl

def check_non_breaking_space():
    wb = openpyxl.load_workbook('check_non_breaking_space.xlsx')
    ws = wb['NBSP']

    ws_max_row = ws.max_row
    a, b = [], []
    for _row in ws.iter_rows(min_row=1, max_row=ws_max_row, values_only=True):
        a.append(_row[0])
        b.append(_row[1])

    for _a in a:
        for _b in b:
            f = _a == _b
            print(f"{_a!r} - {_b!r} : {f}") # !R は、repr()の省略記号
            # print(f"{repr(_a)} - {repr(_b)} : {f}")

    normal_space = "hello world"
    nbsp = "hello\u00A0world"
    nbsp2 = "hello\xA0world"

    print(normal_space)       # hello world
    print(nbsp)               # hello world  （見た目では判別しづらい）
    print(nbsp2)               # hello world  （見た目では判別しづらい）

    print(repr(normal_space)) # 'hello world'
    print(repr(nbsp))         # 'hello\xa0world'
    print(repr(nbsp2))         # 'hello\xa0world'

def main():
    check_non_breaking_space()

if __name__ == "__main__":
    main()