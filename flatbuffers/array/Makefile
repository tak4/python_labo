#ターゲット名:	依存関係ファイル
#				コマンド
#ターゲット名は gcc -o の代わり

CC=g++
CFLAG=-g -Wall -I/home/takashi/develop/flatbuffers/include

all	:			deserialize_sample154
deserialize_sample154:	deserialize_sample154.o
			$(CC) $(CFLAG) deserialize_sample154.o -o deserialize_sample154

deserialize_sample154.o:	deserialize_sample154.cpp
			$(CC) $(CFLAG) -c deserialize_sample154.cpp

.PHONY : clean
clean:
# @はコンソールに表示しない為の指示
	@rm -f *.o

