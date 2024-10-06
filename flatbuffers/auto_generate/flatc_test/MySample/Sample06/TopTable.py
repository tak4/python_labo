# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample06

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
    def Bfeilda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # TopTable
    def Ubfeilda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # TopTable
    def Bofielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TopTable
    def Sfielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # TopTable
    def Usfielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # TopTable
    def Ifielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TopTable
    def Uifielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # TopTable
    def Ffielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TopTable
    def Lfielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TopTable
    def Ulfielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # TopTable
    def Dfielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # TopTable
    def Stfielda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def TopTableStart(builder): builder.StartObject(12)
def TopTableAddBfeilda(builder, bfeilda): builder.PrependInt8Slot(0, bfeilda, 0)
def TopTableAddUbfeilda(builder, ubfeilda): builder.PrependUint8Slot(1, ubfeilda, 0)
def TopTableAddBofielda(builder, bofielda): builder.PrependBoolSlot(2, bofielda, 0)
def TopTableAddSfielda(builder, sfielda): builder.PrependInt16Slot(3, sfielda, 0)
def TopTableAddUsfielda(builder, usfielda): builder.PrependUint16Slot(4, usfielda, 0)
def TopTableAddIfielda(builder, ifielda): builder.PrependInt32Slot(5, ifielda, 0)
def TopTableAddUifielda(builder, uifielda): builder.PrependUint32Slot(6, uifielda, 0)
def TopTableAddFfielda(builder, ffielda): builder.PrependFloat32Slot(7, ffielda, 0.0)
def TopTableAddLfielda(builder, lfielda): builder.PrependInt64Slot(8, lfielda, 0)
def TopTableAddUlfielda(builder, ulfielda): builder.PrependUint64Slot(9, ulfielda, 0)
def TopTableAddDfielda(builder, dfielda): builder.PrependFloat64Slot(10, dfielda, 0.0)
def TopTableAddStfielda(builder, stfielda): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(stfielda), 0)
def TopTableEnd(builder): return builder.EndObject()
