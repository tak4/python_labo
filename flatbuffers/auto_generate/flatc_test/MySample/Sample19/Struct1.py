# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample19

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Struct1(object):
    __slots__ = ['_tab']

    # Struct1
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Struct1
    def Ffielda(self): return [self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0 + i * 4)) for i in range(3)]
    # Struct1
    def FfieldaLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(0))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Struct1
    def FfieldaIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(0))
        return o == 0


def CreateStruct1(builder, ffielda):
    builder.Prep(4, 12)
    for _idx0 in range(3 , 0, -1):
        builder.PrependFloat32(ffielda[_idx0-1])
    return builder.Offset()
