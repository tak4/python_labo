import os
import sys
import base64
import json

base_path = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__))))
sys.path.append(base_path)
from SmartCamera import BoundingBox
from SmartCamera import BoundingBox2d
from SmartCamera import ObjectDetectionTop

def main():

    with open('output/object_detection_decode.bin', 'rb') as f:
        buf = f.read()
        buf = bytearray(buf)
    print(buf)

    ppl_out = ObjectDetectionTop.ObjectDetectionTop.GetRootAsObjectDetectionTop(buf, 0)
    obj_data = ppl_out.Perception()
    res_num = obj_data.ObjectDetectionListLength()
    print(res_num)

    for i in range(res_num):
        obj_list = obj_data.ObjectDetectionList(i)
        union_type = obj_list.BoundingBoxType()
        if union_type == BoundingBox.BoundingBox.BoundingBox2d:
            bbox_2d = BoundingBox2d.BoundingBox2d()
            bbox_2d.Init(obj_list.BoundingBox().Bytes, obj_list.BoundingBox().Pos)
            print(obj_list.ClassId())
            print(round(obj_list.Score(), 6))
            print(bbox_2d.Left())
            print(bbox_2d.Top())
            print(bbox_2d.Right())
            print(bbox_2d.Bottom())

    # bbox_2d = BoundingBox2d.BoundingBox2d()
    # print(bbox_2d.Left())

if __name__ == '__main__':
    main()
