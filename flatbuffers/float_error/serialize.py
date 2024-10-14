import flatbuffers
import os

from Sample import TopTable



def main():
    builder = flatbuffers.Builder(0)

    TopTable.TopTableStart(builder)
    TopTable.TopTableAddFVal(builder, 0.1)
    TopTable.TopTableAddDVal(builder, 0.1)
    toptable = TopTable.TopTableEnd(builder)

    builder.Finish(toptable)
    buf = builder.Output()

    with open('output.bin', 'wb') as f:
        f.write(buf)

if __name__ == '__main__':
   main()
