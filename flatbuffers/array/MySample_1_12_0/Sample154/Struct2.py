# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample154

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Struct2(object):
    __slots__ = ['_tab']

    # Struct2
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Struct2
    def Sint32(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))

def CreateStruct2(builder, sint32):
    builder.Prep(4, 4)
    builder.PrependUint32(sint32)
    return builder.Offset()
