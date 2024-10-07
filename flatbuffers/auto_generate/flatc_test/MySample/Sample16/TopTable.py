# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample16

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TopTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTopTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TopTable()
        x.Init(buf, n + offset)
        return x

    # TopTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TopTable
    def Structa(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from MySample.Sample16.Struct1 import Struct1
            obj = Struct1()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def TopTableStart(builder): builder.StartObject(1)
def TopTableAddStructa(builder, structa): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(structa), 0)
def TopTableEnd(builder): return builder.EndObject()
