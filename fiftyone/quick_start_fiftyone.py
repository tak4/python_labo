# https://docs.voxel51.com/getting_started/install.html#quickstart
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")
session = fo.launch_app(dataset)

session.wait()
