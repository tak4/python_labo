# flatbuffers

https://flatbuffers.dev/

https://github.com/google/flatbuffers


## clone

git clone https://github.com/google/flatbuffers.git


## build

cmake -G "Unix Makefiles"
make -j


## flatc

../flatbuffers/flatc --python monster.fbs


## serialize / deserialize

cd sample

python3 serialize.py

python3 deserialize.py

