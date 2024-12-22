# https://docs.voxel51.com/dataset_zoo/datasets.html#cifar-10
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("cifar10", split="test")

session = fo.launch_app(dataset)
