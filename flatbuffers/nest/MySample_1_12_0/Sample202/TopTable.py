# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample202

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
    def Table1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from MySample.Sample202.Table1 import Table1
            obj = Table1()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def TopTableStart(builder): builder.StartObject(1)
def TopTableAddTable1(builder, table1): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(table1), 0)
def TopTableEnd(builder): return builder.EndObject()
