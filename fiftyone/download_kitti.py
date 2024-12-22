import fiftyone as fo
import fiftyone.utils.kitti

# KITTIデータセットをダウンロード
download_kitti("path/to/save/dataset")

# ダウンロードしたデータセットをFiftyOneのDatasetオブジェクトとして読み込む
dataset = fo.Dataset.from_dir("path/to/save/dataset", dataset_type=fo.DatasetType.KITTI)
