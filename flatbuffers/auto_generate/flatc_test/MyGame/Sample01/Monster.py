# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample01

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Monster(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMonster(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Monster()
        x.Init(buf, n + offset)
        return x

    # Monster
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Monster
    def Mana(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Hp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def MonsterStart(builder): builder.StartObject(4)
def MonsterAddMana(builder, mana): builder.PrependInt16Slot(0, mana, 0)
def MonsterAddHp(builder, hp): builder.PrependInt16Slot(1, hp, 0)
def MonsterAddName(builder, name): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def MonsterEnd(builder): return builder.EndObject()
