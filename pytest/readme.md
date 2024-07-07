# フォルダ校正
├── target  
テスト対象  
├── test  
テスト対象＋テストコード  
├── test_target  
targetのテストコード  

# テスト実行
## print出力

pytest -s test

## テストエラー時にデバッガ起動

pytest -pdb test

## テストの実行時間を出力する
### https://docs.pytest.org/en/7.1.x/how-to/usage.html#profiling-test-execution-duration

pytest --durations=0 test
