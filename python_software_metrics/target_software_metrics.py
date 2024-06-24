def test_function1():
    print('hello world')

def test_function2(flg):
    if flg:
        print('branch a')
    else:
        print('branch b')

def test_function3(stage):
    if stage == 0:
        print('branch a')
    elif stage == 1:
        print('branch b')
    else:
        print('branch c')

def test_function4(loop_num):
   for i in range(loop_num):
    print(f'{i}')

def test_function5():
   with open('test.txt', 'w') as f:
      f.write('test')

def calculate_average(numbers):
  if len(numbers) == 0:
    return 0
  else:
    total = 0
    for number in numbers:
      total += number
    return total / len(numbers)


test_function1()
test_function2(True)
test_function3(0)
test_function4(10)
test_function5()

average = calculate_average([1, 2, 3, 4, 5])
print(average)
