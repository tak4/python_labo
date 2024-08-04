# フォルダ構成
├── target  
テスト対象  
├── test  
テスト対象＋テストコード  
├── test_target  
targetのテストコード  

# テスト実行
## print出力

`pytest -s test`

## テストエラー時にデバッガ起動

`pytest -pdb test`

## テストの実行時間を出力する

`pytest --durations=0 test`

参考  
https://docs.pytest.org/en/7.1.x/how-to/usage.html#profiling-test-execution-duration


## vscode setting.json

.vscode/settings.json
```
{
    "python.testing.pytestArgs": [
        ".",
        "-s",
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

## 環境変数を設定する

pytest-env
pytest のプラグイン  
https://pypi.org/project/pytest-env/

プロジェクト直下に下記ファイルを作成して環境変数の内容を記載する  
pytest.ini

## カバレッジ

pytest-cov  
pytest のプラグイン
https://pypi.org/project/pytest-cov/
https://pytest-cov.readthedocs.io/en/latest/index.html

### C0
- テスト対象：test_target  
- カバレッジ取得対象：test_target  
`pytest ./test_target --cov=test_target --cov-report=html`  

- テスト対象：test  
- カバレッジ取得対象：test_target  
`pytest ./test --cov=test_target --cov-report=html`  
-> カバレッジ取得対象がテストされていないので、カバレッジ0%  

### C1
- テスト対象：test_target  
- カバレッジ取得対象：test_target  
`pytest ./test_target --cov=test_target --cov-branch --cov-report=html`  

