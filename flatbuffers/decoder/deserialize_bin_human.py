import generate.Human.Human


def main():

    with open('output_human.bin', 'rb') as f:
      buf = f.read()
      buf = bytearray(buf)

    human = generate.Human.Human.Human.GetRootAsHuman(buf, 0)

    print(human.Name())
    print(human.Age())


if __name__ == '__main__':
  main()
