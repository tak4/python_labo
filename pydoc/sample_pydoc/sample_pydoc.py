"""pydocのサンプル"""

class Customer_reStructuredTextStyle:
    """顧客クラス
    
    :ivar name: 氏名
    :type name: str
    :ivar address: 住所
    :type address: str
    """

    def __init__(self, name:str, address:str):
        self.name = name
        self.address = address


class Customer_GoolgeStyle:
    """顧客クラス
    
    Attributes:
        name (str): 氏名
        address (str): 住所
    """

    def __init__(self, name:str, address:str):
        self.name = name
        self.address = address


def total_amount_restructure_text_style(
        amount:int, postage:int, tax_rate:float
) -> int:
    """支払合計を計算
    
    :param amount: 商品購入金額
    :type amount: int
    :param postage: 送料
    :type postage: int
    :param tax_rate: 税率
    :type tax_rate: float
    :return: 支払合計金額
    :rtype: int
    """
    total = (amount + postage) * (1 + tax_rate)
    return int(total)

def total_amount_google_style(
        amount:int, postage:int, tax_rate:float
) -> int:
    """支払合計を計算

    Args:
        amount (int): 商品購入金額
        postage (int): 送料
        tax_rage (float): 税率
    Returns:
        int: 支払い合計金額
    """
    total = (amount + postage) * (1 + tax_rate)
    return int(total)



def example_func(param1, param2): 
    """Example function with types documented in the docstrings.
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for scucess, False otherwise.
    """

    print(param1)
    print(param2)

    return True

# Consoleに表示する
# print(example_func.__doc__)
# manコマンドのように表示する
# print(help(example_func))

if __name__ == '__main__':
    example_func('param1', 'param2')