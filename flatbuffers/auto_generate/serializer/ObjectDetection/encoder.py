import base64
import flatbuffers
import json
import os
import sys
base_path = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__))))
sys.path.append(base_path)
from SmartCamera import ObjectDetectionTop
from SmartCamera import ObjectDetectionData
from SmartCamera import GeneralObject
from SmartCamera import BoundingBox
from SmartCamera import BoundingBox2d

def main():
    # バッファーの初期サイズ0
    # 必要に応じて拡張されるらしい
    builder = flatbuffers.Builder(0)

    # table BoundingBox2d を作成
    BoundingBox2d.BoundingBox2dStart(builder)
    BoundingBox2d.BoundingBox2dAddLeft(builder, 10)
    BoundingBox2d.BoundingBox2dAddTop(builder, 20)
    BoundingBox2d.BoundingBox2dAddRight(builder, 30)
    BoundingBox2d.BoundingBox2dAddBottom(builder, 40)
    bounding_box_2d = BoundingBox2d.BoundingBox2dEnd(builder)

    # union BoundingBox を作成
    # BoundingBoxType は、schema上には存在しないが、BoundingBoxのメタデータとして付与するものあらしい
    # deserialize時に参照可能
    GeneralObject.GeneralObjectStart(builder)
    GeneralObject.GeneralObjectAddClassId(builder, 100)
    GeneralObject.GeneralObjectAddBoundingBox(builder, bounding_box_2d)
    GeneralObject.GeneralObjectAddBoundingBoxType(builder, BoundingBox.BoundingBox.BoundingBox2d)
    GeneralObject.GeneralObjectAddScore(builder, 200.00)
    general_object = GeneralObject.GeneralObjectEnd(builder)

    # object_detection_list:[GeneralObject]; を作成
    object_detection_data_num = 5
    ObjectDetectionData.ObjectDetectionDataStartObjectDetectionListVector(
        builder, object_detection_data_num)
    for _ in range(object_detection_data_num):
        builder.PrependSOffsetTRelative(general_object) # テストなので同じデータを複数個設定
    object_detecion_list = builder.EndVector()

    # table ObjectDetectionData を作成
    ObjectDetectionData.ObjectDetectionDataStart(builder)
    ObjectDetectionData.ObjectDetectionDataAddObjectDetectionList(builder, object_detecion_list)
    object_detection_data = ObjectDetectionData.ObjectDetectionDataEnd(builder)

    # table ObjectDetectionTop を作成
    ObjectDetectionTop.ObjectDetectionTopStart(builder)
    ObjectDetectionTop.ObjectDetectionTopAddPerception(builder, object_detection_data)
    od = ObjectDetectionTop.ObjectDetectionTopEnd(builder)

    builder.Finish(od)

    # Output the buffer data
    buf = builder.Output()

    # Write the binary data to a file
    output_dir = os.path.dirname(__file__)
    output_bin = os.path.join(output_dir, base_path + '/output/object_detection_decode.bin')
    with open(output_bin, 'wb') as f:
        f.write(buf)

    # base64エンコード
    encord_bytes = base64.b64encode(buf)  # base64エンコードして、bytes型を返す
    base64s = encord_bytes.decode() # str型に変換

    # json 出力
    json_data = {'data': base64s}

    output_dir = os.path.dirname(__file__)
    output_json = os.path.join(output_dir, base_path + '/output/object_detection_decode.json')
    with open(output_json, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
   main()
