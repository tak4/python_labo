class PropertyClass:
      def __init__(self, msg):
        self.__message = msg
  
      def __str__(self):
        return self.message
    
      @property
      def message(self):
        return self.__message
    
      @message.setter
      def message(self, value):
        if value != '':
          self.__message = value
      

pc= PropertyClass('Hello')   #  ①
print(pc.message)   # Hello　②
pc.message = ''   # messageの中身を「Hello」から空文字列に変更   ③
print(pc)   # Hello  ④
pc.message = 'Bye!'   # messageの中身を「Hello」から「Bye!」に変更   ⑤
print(pc)   # Bye!   ⑥
