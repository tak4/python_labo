# https://docs.voxel51.com/user_guide/using_views.html#dataset-views
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("kitti-multiview")

view = dataset.view()

print(view)