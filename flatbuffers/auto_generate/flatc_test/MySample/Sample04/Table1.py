# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample04

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
    def Ifielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Table1
    def Color(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def Table1Start(builder): builder.StartObject(2)
def Table1AddIfielda(builder, ifielda): builder.PrependInt32Slot(0, ifielda, 0)
def Table1AddColor(builder, color): builder.PrependInt8Slot(1, color, 0)
def Table1End(builder): return builder.EndObject()
