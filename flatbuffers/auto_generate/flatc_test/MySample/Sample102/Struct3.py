# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample102

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Struct3(object):
    __slots__ = ['_tab']

    # Struct3
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Struct3
    def Ifielda(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))

def CreateStruct3(builder, ifielda):
    builder.Prep(4, 4)
    builder.PrependInt32(ifielda)
    return builder.Offset()