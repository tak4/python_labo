# github
flatbuffers_24_3_25/

# make
cmake -G "Unix Makefiles"
make -j

# cpp コード生成
flatc --cpp ./schema/sample154.fbs  

# makefile include path追加

https://github.com/google/flatbuffers/tree/master
をcloseした場所へinclude path指定する

-I/home/takashi/develop/flatbuffers/include

# Compie error

float_double_generated.h: In member function ‘bool Sample::TopTable::Verify(flatbuffers::Verifier&) const’:
float_double_generated.h:28:30: error: no matching function for call to ‘Sample::TopTable::VerifyField<float>(flatbuffers::Verifier&, Sample::TopTable::FlatBuffersVTableOffset) const’
   28 |            VerifyField<float>(verifier, VT_F_VAL) &&
      |            ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
In file included from /home/takashi/develop/flatbuffers/include/flatbuffers/flatbuffer_builder.h:36,
                 from /home/takashi/develop/flatbuffers/include/flatbuffers/flatbuffers.h:29,
                 from float_double_generated.h:7,
                 from serialize.cpp:1:


# Compile error

g++ -g -Wall -I/home/takashi/develop/flatbuffers/include -c deserialize_sample154.cpp
In file included from deserialize_sample154.cpp:5:
sample154_generated.h: In member function ‘bool MySample::Sample154::TopTable::Verify(flatbuffers::Verifier&) const’:
sample154_generated.h:60:52: error: no matching function for call to ‘MySample::Sample154::TopTable::VerifyField<MySample::Sample154::Table1>(flatbuffers::Verifier&, MySample::Sample154::TopTable::FlatBuffersVTableOffset) const’
   60 |            VerifyField<MySample::Sample154::Table1>(verifier, VT_TABLE1) &&
      |            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~
In file included from /home/takashi/develop/flatbuffers/include/flatbuffers/flatbuffer_builder.h:36,
                 from /home/takashi/develop/flatbuffers/include/flatbuffers/flatbuffers.h:29,
                 from sample154_generated.h:7,
                 from deserialize_sample154.cpp:5:
/home/takashi/develop/flatbuffers/include/flatbuffers/table.h:125:8: note: candidate: ‘bool flatbuffers::Table::VerifyField(const flatbuffers::Verifier&, flatbuffers::voffset_t, size_t) const [with T = MySample::Sample154::Table1; flatbuffers::voffset_t = short unsigned int; size_t = long unsigned int]’
  125 |   bool VerifyField(const Verifier &verifier, voffset_t field,
      |        ^~~~~~~~~~~
/home/takashi/develop/flatbuffers/include/flatbuffers/table.h:125:8: note:   candidate expects 3 arguments, 2 provided
deserialize_sample154.cpp: In function ‘int main(int, char**)’:
deserialize_sample154.cpp:54:30: error: ‘const struct MySample::Sample154::Table1’ has no member named ‘struct1_length’
   54 |         int length = table1->struct1_length();
      |                              ^~~~~~~~~~~~~~
make: *** [Makefile:13: deserialize_sample154.o] Error 1



## 修正前
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<MySample::Sample154::Table1>(verifier, VT_TABLE1) &&
           verifier.EndTable();
  }


## 修正後
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<MySample::Sample154::Table1>(verifier, VT_TABLE1, sizeof(MySample::Sample154::Table1)) &&
           verifier.EndTable();
  }
