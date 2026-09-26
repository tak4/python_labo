import argparse
from difflib import SequenceMatcher
from html import escape
from string import Template
import openpyxl

page_template = Template("""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
body { font-family: sans-serif; }
.equal { background-color: #f2aaf8; }
.changed { background-color: #fff3a3; }
.deleted { background-color: #ffb3b3; text-decoration: line-through; }
.added { background-color: #b3ffb3; }
th {
    border-width: 1px;
}
td {
    border-width: 1px;
}
</style>
</head>
<body>
    <table>
    $comparisons
    </table>
</body>
</html>
""")

def create_pair_html(result_list: list, idx: int) -> str:
    index_a = result_list[0]
    text_a = result_list[1]
    index_b = result_list[2]
    text_b = result_list[3]
    ratio = result_list[4]
    matcher = SequenceMatcher(None, text_a, text_b)

    text_a_html = []
    text_b_html = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            text = escape(text_a[i1:i2])
            text_a_html.append(text)
            text_b_html.append(f'<span class="equal">{text}</span>')

        elif tag == "replace":
            text_a_part = escape(text_a[i1:i2])
            text_b_part = escape(text_b[j1:j2])

            # text_a_html.append(f'<span class="changed">{old_part}</span>')
            # text_b_html.append(f'<span class="changed">{new_part}</span>')
            text_a_html.append(text_a_part)
            text_a_html.append(text_b_part)

        elif tag == "delete":
            text = escape(text_a[i1:i2])
            # text_a_html.append(f'<span class="deleted">{text}</span>')
            text_a_html.append(text)

        elif tag == "insert":
            text = escape(text_b[j1:j2])
            # text_b_html.append(f'<span class="added">{text}</span>')
            text_b_html.append(text)

    return f"""
    <div class="comparison">
        <tr>
            <td>{idx}</td>
            <td>{index_a}</td>
            <td>{''.join(text_a_html)}</td>
            <td>{index_b}</td>
            <td>{''.join(text_b_html)}</td>
            <td>{ratio}</td>
        </tr>
    </div>
    """

def create_diff_page(comparison_list: list):
    sections = []
    for idx, result_list in enumerate(comparison_list, 1):
        sections.append(create_pair_html(result_list, idx))
    return page_template.substitute(comparisons="".join(sections))

def create_comparison_list(
        result_wb_name: str,
        result_ws_name: str,
        input_data_start_row: int,
        result_criteria_index_col: int,
        result_criteria_data_col: int,
        result_target_index_col: int,
        result_target_data_col: int,
        result_ratio_col: int,
        ):

    result_wb_name = openpyxl.load_workbook(result_wb_name)
    result_ws_name = result_wb_name[result_ws_name]

    comparison_list = []
    result_ws_max_row = result_ws_name.max_row
    for criteria_row in result_ws_name.iter_rows(min_row=input_data_start_row, max_row=result_ws_max_row, values_only=True):
        if criteria_row[result_criteria_data_col-1] is None:
            continue
        criteria_index_no = criteria_row[result_criteria_index_col-1]
        criteria_line = str(criteria_row[result_criteria_data_col-1]).strip()
        target_index_no = criteria_row[result_target_index_col-1]
        target_line = str(criteria_row[result_target_data_col-1]).strip()
        result_ratio = str(criteria_row[result_ratio_col-1]).strip()
        if not criteria_line:
            continue
        comparison_list.append([criteria_index_no,criteria_line,target_index_no,target_line,result_ratio])

    return comparison_list


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--result_wb", type=str, default="./process/output/result_split_org_wb.xlsx", help="比較結果のワークブック")
    parser.add_argument("--result_ws", type=str, default="result", help="比較結果リストのシート名")
    parser.add_argument("--input_data_start_row", type=int, default=2, help="データの開始行")
    parser.add_argument("--result_criteria_index_col", type=int, default=1, help="比較結果リストの項番の列番号")
    parser.add_argument("--result_criteria_data_col", type=int, default=2, help="比較結果リストのデータの列番号")
    parser.add_argument("--result_target_index_col", type=int, default=3, help="比較対象リストの項番の列番号")
    parser.add_argument("--result_target_data_col", type=int, default=4, help="比較対象リストのデータの列番号")
    parser.add_argument("--result_ratio_col", type=int, default=5, help="比較対象リストのデータの列番号")

    parser.add_argument("--output_dir", type=str, default="./process/output", help="出力先ディレクトリ")

    args = parser.parse_args()

    comparison_list = create_comparison_list(
        args.result_wb, 
        args.result_ws, 
        args.input_data_start_row, 
        args.result_criteria_index_col, 
        args.result_criteria_data_col, 
        args.result_target_index_col, 
        args.result_target_data_col,
        args.result_ratio_col
        )

    html = create_diff_page(comparison_list)

    with open("diff.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()
