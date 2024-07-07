# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Human

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Human(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsHuman(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Human()
        x.Init(buf, n + offset)
        return x

    # Human
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Human
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Human
    def Age(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def HumanStart(builder): builder.StartObject(2)
def HumanAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def HumanAddAge(builder, age): builder.PrependInt16Slot(1, age, 0)
def HumanEnd(builder): return builder.EndObject()
