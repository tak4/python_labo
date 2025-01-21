import fiftyone as fo
import fiftyone.zoo as foz

import multiprocessing
# CPUコア数を取得 num_workersを指定しなかった場合の値
cpu_cores = multiprocessing.cpu_count()
print(f"使用可能なCPUコア数: {cpu_cores}")

# https://docs.voxel51.com/dataset_zoo/datasets.html#open-images-v6
dataset = foz.load_zoo_dataset(
    "open-images-v6",
    split="train",
    label_types="detections",
    classes="Bird",
    max_samples=10,
    shuffle=False,
    overwrite=True
)
