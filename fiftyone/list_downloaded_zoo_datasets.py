# https://docs.voxel51.com/dataset_zoo/api.html#listing-zoo-datasets
import fiftyone as fo
import fiftyone.zoo as foz

# ダウンロード済みデータセットの一覧
downloaded_datasets = foz.list_downloaded_zoo_datasets()
fo.pprint(downloaded_datasets)

