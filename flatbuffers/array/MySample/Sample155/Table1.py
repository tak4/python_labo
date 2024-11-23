# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample155

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Table1(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Table1()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTable1(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Table1
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Table1
    def Struct1(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            from MySample.Sample155.Struct1 import Struct1
            obj = Struct1()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Table1
    def Struct1Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Table1
    def Struct1IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def Table1Start(builder):
    builder.StartObject(1)

def Start(builder):
    Table1Start(builder)

def Table1AddStruct1(builder, struct1):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(struct1), 0)

def AddStruct1(builder, struct1):
    Table1AddStruct1(builder, struct1)

def Table1StartStruct1Vector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartStruct1Vector(builder, numElems):
    return Table1StartStruct1Vector(builder, numElems)

def Table1End(builder):
    return builder.EndObject()

def End(builder):
    return Table1End(builder)