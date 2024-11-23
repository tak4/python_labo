# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample153

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Table1(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTable1(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Table1()
        x.Init(buf, n + offset)
        return x

    # Table1
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Table1
    def Table2(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from MySample.Sample153.Table2 import Table2
            obj = Table2()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Table1
    def Table2Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Table1
    def Table2IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def Table1Start(builder): builder.StartObject(1)
def Table1AddTable2(builder, table2): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(table2), 0)
def Table1StartTable2Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def Table1End(builder): return builder.EndObject()