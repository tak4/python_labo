# https://docs.voxel51.com/dataset_zoo/api.html#listing-zoo-datasets
import fiftyone.zoo as foz

# Buildin Datasetのリストを取得
available_datasets = foz.list_zoo_datasets()

for dataset in available_datasets:
    print(dataset)
