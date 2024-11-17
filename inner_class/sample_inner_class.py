class Data:
    def __init__(self, data):
        self.data = data

    class Iterator:
        def __init__(self, data):
            self.data = data
            self.index = 0

        def __next__(self):
            if self.index >= len(self.data):
                raise StopIteration
            value = self.data[self.index]
            self.index += 1
            return value

    def __iter__(self):
        return self.Iterator(self.data)


if __name__ == "__main__":

    # データのイテレーション
    data = Data([1, 2, 3])
    for item in data:
        print(item)