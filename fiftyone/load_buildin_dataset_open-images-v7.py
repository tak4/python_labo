import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "open-images-v7",
    split="train",
    max_samples=10,
    shuffle=False,
    overwrite=True
)

