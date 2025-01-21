# https://docs.voxel51.com/dataset_zoo/api.html#getting-information-about-zoo-datasets
import textwrap
import fiftyone as fo
import fiftyone.zoo as foz

dataset_name = 'cifar10'

# get info
zoo_dataset = foz.get_zoo_dataset(dataset_name)

print("***** Dataset description *****")
print(textwrap.dedent("    " + zoo_dataset.__doc__))

print("***** Tags *****")
print("%s\n" % ", ".join(zoo_dataset.tags))

print("***** Supported splits *****")
print("%s\n" % ", ".join(zoo_dataset.supported_splits))

# https://docs.voxel51.com/api/fiftyone.utils.openimages.html#fiftyone.utils.openimages.get_classes
oiv7_classes = fo.utils.openimages.get_classes(version='v7', dataset_dir=None)
for name in oiv7_classes:
    print(name)

# download
# dataset_dir = foz.find_zoo_dataset(dataset_name)
# info = foz.load_zoo_dataset_info(dataset_name)

# print("***** Dataset location *****")
# print(dataset_dir)

# print("\n***** Dataset info *****")
# print(info)