# CUSTOM 9FIN MODULE
# doc-layout dataset definition
from mmdet.registry import DATASETS

from .coco import CocoDataset


@DATASETS.register_module()
class DocLayDataset(CocoDataset):
    """Customized Dataset for COCO detection format."""

    METAINFO = {
        "classes": ("Title", "Text", "Figure", "Table", "List"),
        "palette": [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (0, 255, 255),
        ],
    }
