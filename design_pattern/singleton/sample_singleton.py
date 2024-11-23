# Singleton の検証

# newメソッドドキュメント
# https://docs.python.org/ja/3.13/reference/datamodel.html#object.__new__
# superクラス ドキュメント
# https://docs.python.org/ja/3.13/library/functions.html#super

class NotSingleton():
    '''
    Singletonではないクラス
    value というプロパティを持つ
    value の初期値は 0
    value には 0 は設定できない
    '''

    def __init__(self):
        self.__value = 100

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        if v != 0:
            self.__value = v


class Singleton():
    '''
    Singletonのクラス
    value というプロパティを持つ
    value の初期値は 0
    value には 0 は設定できない
    '''

    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            print(f'type(cls._instance): {type(cls._instance)}')

        return cls._instance

    def __init__(self):
        self.__value = 100

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        if v != 0:
            self.__value = v



class SingletonInitParam():
    '''
    Singletonのクラス
    value というプロパティを持つ
    value の初期値は コンストラクタで指定可能
    value には 0 は設定できない
    '''

    _instance = None
    
    # __init__にパラメータ v がある場合、__new__でも,その引数を受ける為、*argsは必要。
    # キーワード引数を受ける場合も想定して、*args, **kwargs と書くのが慣例っぽい
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print(f'type(cls._instance): {type(cls._instance)}')

        return cls._instance

    def __init__(self, v):
        '''
        シングルトンクラスのコンストラクタに引数があるのは、必ずしも設計としておかしいとは言えません。
        しかし、シングルトンパターンの目的を考えると、注意が必要であり、初期化処理を別のメソッドで行う方が、より適切な設計であることが多いです。
        コンストラクタに引数を指定する場合は、引数はインスタンスの状態ではなく、初期化処理にのみ使用し、引数の値はシングルトン全体で共通にする必要があります。
        '''
        self.__value = v

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        if v != 0:
            self.__value = v


class Myclass(Singleton):
    def __init__(self, input):
        self.input = input


def main():

    # 非Singleton
    not_singleton_a = NotSingleton()
    not_singleton_b = NotSingleton()
    not_singleton_b.value = 400
    print(not_singleton_a == not_singleton_b)
    print(f'not_singleton_a.value: {not_singleton_a.value}')
    print(f'not_singleton_b.value: {not_singleton_b.value}')
    print()

    # Singleton
    singleton_a = Singleton()
    singleton_b = Singleton()
    singleton_b.value = 400
    print(singleton_a == singleton_b)
    print(f'singleton_a.value: {singleton_a.value}')
    print(f'singleton_b.value: {singleton_b.value}')
    print()

    # Singleton コンストラクタパラメータあり
    singleton_init_param_a = SingletonInitParam(100)
    singleton_init_param_b = SingletonInitParam(200)
    print(singleton_init_param_a == singleton_init_param_b)
    print(f'singleton_init_param_a.value: {singleton_init_param_a.value}')
    print(f'singleton_init_param_a.value: {singleton_init_param_b.value}')

    # Singleton コンストラクタキーワードパラメータあり
    singleton_init_param_a = SingletonInitParam(v=100)
    singleton_init_param_b = SingletonInitParam(v=200)
    print(singleton_init_param_a == singleton_init_param_b)
    print(f'singleton_init_param_a.value: {singleton_init_param_a.value}')
    print(f'singleton_init_param_a.value: {singleton_init_param_b.value}')


if __name__ == '__main__':

    main()

    # one = Myclass(1)
    # print("one.input={0}".format(one.input))
    # two = Myclass(2)
    # print("one.input={0}, two.input={1}".format(one.input, two.input))
    # one.input = 0
    # print("one.input={0}, two.input={1}".format(one.input, two.input))
