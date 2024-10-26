# private メソッドのオーバーライドを試す
import abc

class Base:
    @abc.abstractmethod
    def showa(self):
        pass

    def show(self):
        print('Base class showa()')
        self.__show()
    
    def __show(self):
        print('Base class __showa()')

class Derived(Base):
    def showa(self):
        print('Derived class showa()')

    def show(self):
        print('Derived class show()')
        self.__show()

    def __show(self):
        print('Derived class __show()')


def main():
    base = Derived()
    base.showa()
    base.show()
    # base.__show()         # 呼び出し不可
    base._Derived__show()   # マングリングされた名称で呼び出し可能

if __name__ == '__main__':
    main()
