# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample150

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Struct1(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 12

    # Struct1
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Struct1
    def Sint32(self, j = None):
        if j is None:
            return [self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0 + i * 4)) for i in range(self.Sint32Length())]
        elif j >= 0 and j < self.Sint32Length():
            return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0 + j * 4))
        else:
            return None

    # Struct1
    def Sint32AsNumpy(self):
        return self._tab.GetArrayAsNumpy(flatbuffers.number_types.Int32Flags, self._tab.Pos + 0, self.Sint32Length())

    # Struct1
    def Sint32Length(self):
        return 3

    # Struct1
    def Sint32IsNone(self):
        return False


def CreateStruct1(builder, sint32):
    builder.Prep(4, 12)
    for _idx0 in range(3 , 0, -1):
        builder.PrependInt32(sint32[_idx0-1])
    return builder.Offset()