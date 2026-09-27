# 実行
python -m pre_process.split_multiline_cell --input_wb ./input_data/criteria_wb.xlsx

python -m pre_process.split_multiline_cell --input_wb ./input_data/target_wb.xlsx

python -m process.string_comparison --criteria_wb ./pre_process/output/split_list_criteria_wb.xlsx --target_wb ./pre_process/output/split_list_target_wb.xlsx

python -m post_process.generate_diff_string --result_wb ./process/output/result_split_list_criteria_wb.xlsx
