# https://docs.voxel51.com/dataset_zoo/datasets.html#kitti
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("kitti", split="train")

session = fo.launch_app(dataset)