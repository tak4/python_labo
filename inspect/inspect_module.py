import sys
import inspect

def get_class_info(module_name):
    """
    指定したモジュールのクラス名とメンバ情報を取得する関数

    Args:
        module_name (str): モジュール名

    Returns:
        dict: クラス名とメンバ情報の辞書。
            キー: クラス名
            値: (メンバ変数のリスト, メソッドのリスト)
    """

    module = __import__(module_name)
    class_info = {}

    for name, obj in inspect.getmembers(module):        
        if inspect.isclass(obj):
            members = inspect.getmembers(obj)
            class_info[name] = (
                [attr for attr, value in members if not inspect.ismethod(value)],
                [method for method, value in members if inspect.ismethod(value)]
            )

    return class_info

if __name__ == "__main__":

    # モジュール名取得
    if len(sys.argv) <= 1:
        print('Please specify module name')
        exit()

    print('--- sys.path start ---')
    for p in sys.path:
        print(p)
    print('--- sys.path end   ---')
    print()

    module_name = sys.argv[1]

    result = get_class_info(module_name)

    for class_name, (attributes, methods) in result.items():
        print(f"クラス名: {class_name}")
        print("属性:")
        for attr in attributes:
            print(f"  - {attr}")
        print("メソッド:")
        for method in methods:
            print(f"  - {method}")
