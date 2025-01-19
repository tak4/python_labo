# https://docs.voxel51.com/tutorials/cvat_annotation.html#Annotating-Datasets-with-CVAT
import fiftyone as fo
import fiftyone.zoo as foz

# 組み込みの FiftyOne Dataset Zoo を使用して、
# Open Images V6 データセットからいくつかの画像をダウンロードする
dataset = foz.load_zoo_dataset(
    "open-images-v6",
    split="validation",
    label_types=[],
    max_samples=200,
)

import fiftyone.brain as fob

# results = fob.compute_similarity(dataset, brain_key="img_sim")
# results.find_unique(100)

# データセットを永続化して、将来のPythonセッションでアクセスできるようにする
dataset.persistent = True

# FiftyOneアプリで視覚化する
session = fo.launch_app(dataset)

session.freeze() 

session.wait()