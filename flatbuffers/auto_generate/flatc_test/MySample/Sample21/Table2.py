# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample21

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Table2(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTable2(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Table2()
        x.Init(buf, n + offset)
        return x

    # Table2
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Table2
    def Bfielda2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def Table2Start(builder): builder.StartObject(1)
def Table2AddBfielda2(builder, bfielda2): builder.PrependInt8Slot(0, bfielda2, 0)
def Table2End(builder): return builder.EndObject()