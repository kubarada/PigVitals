_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_2x_coco.py'
model = dict(
    backbone=dict(
        type='Res2Net',
        depth=101,
        scales=4,
        base_width=26,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='open-mmlab://res2net101_v1d_26w_4s')))
dataset_type = 'COCODataset'
classes = ('pig_shape',)
data = dict(
    train=dict(
        img_prefix='/storage/plzen1/home/jarada/coco_annotations/images/',
        classes=classes,
        ann_file='/storage/plzen1/home/jarada/coco_annotations/annotations/instances_default.json'),
    val=dict(
        img_prefix='/storage/plzen1/home/jarada/bp_annotations_folder/valid/frames/',
        classes=classes,
        ann_file='/storage/plzen1/home/jarada/bp_annotations_folder/valid/json/instances_default.json'),
    test=dict(
        img_prefix='/storage/plzen1/home/jarada/bp_annotations_folder/test/frames/',
        classes=classes,
        ann_file='/storage/plzen1/home/jarada/bp_annotations_folder/test/json/instances_default.json'))