
class BaseClassA:
    def __init__(self):
        print('BaseClassA.__init__()')
        super().__init__()
    
    def funcA(self):
        print('funcA')

class BaseClassB:
    def __init__(self):
        print('BaseClassB.__init__()')
        super().__init__()

    def funcB(self):
        print('funcB')

class BaseClassC:
    def __init__(self):
        print('BaseClassC.__init__()')
        super().__init__()
    
    def funcC(self):
        print('funcC')


class SubClass(BaseClassA, BaseClassB, BaseClassC):
    def __init__(self):
        print('SubClass.__init__()')
        '''
        メソッド解決順序 (Method Resolution Order, MRO) と呼ばれるルールに従って、
        どの親クラスのメソッドが呼び出されるかが決定される。
        SubClass の場合、MRO は 
        SubClass, BaseClassA, BaseClassB, BaseClassC, object (全てのクラスの基底クラス) の順になる。
        この時、super(BaseClassA, self).__init__() というようにすると、
        BaseClassA の __init__()はSkipされ、BaseClassB, BaseClassC, object の__init__()が呼び出される
        これは下記の目的で使用する。
        ・初期化順序の制御: 複雑な多重継承シナリオでは、親クラスの初期化子の呼び出し順序を細かく制御する必要がある場合があります。このアプローチにより、super() 検索の開始点を明示的に指定し、初期化フローに影響を与えることができます。
        ・特定の親クラスの初期化をスキップ: 何らかの理由で、特定の親クラスの初期化をスキップしたい場合、この手法を使用して、そのクラスの後に super() 検索を開始することで、その __init__ メソッドを効果的にバイパスできます。
        ・古い Python バージョンとの互換性: この明示的な形式の super() は、Python 2 でよく使用されていました。Python 3 でも有効ですが、最新の Python コードでは、よりシンプルな super().__init__() の方が一般的に使用されます。
        '''
        super().__init__()

    def funcSub(self):
        print('funcSub')


s = SubClass()
s.funcA()
s.funcB()
s.funcC()
s.funcSub()


