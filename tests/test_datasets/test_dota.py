# Copyright (c) OpenMMLab. All rights reserved.
import unittest

from mmrotate.datasets import DOTADataset


class TestDOTADataset(unittest.TestCase):

    def test_dota_with_ann_file(self):
        dataset = DOTADataset(
            data_root='tests/dota/data/',
            ann_file='labelTxt/',
            data_prefix=dict(img_path='images/'),
            filter_cfg=dict(
                filter_empty_gt=True, min_size=32, bbox_min_size=32),
            pipeline=[])
        dataset.full_init()
        self.assertEqual(len(dataset), 1)

        data_list = dataset.load_data_list()
        self.assertEqual(len(data_list), 1)
        self.assertEqual(data_list[0]['img_id'], 'P2805__1024__0___0')
        self.assertEqual(data_list[0]['file_name'], 'P2805__1024__0___0.png')
        self.assertEqual(data_list[0]['img_path'],
                         'tests/dota/data/images/P2805__1024__0___0.png')
        self.assertEqual(len(data_list[0]['instances']), 4)
        self.assertEqual(dataset.get_cat_ids(0), [0, 0, 0, 0])

    def test_dota_without_ann_file(self):
        dataset = DOTADataset(
            data_root='tests/data/',
            data_prefix=dict(img_path='images/'),
            filter_cfg=dict(
                filter_empty_gt=True, min_size=32, bbox_min_size=32),
            pipeline=[])
        dataset.full_init()
        self.assertEqual(len(dataset), 1)

        data_list = dataset.load_data_list()
        self.assertEqual(len(data_list), 1)
        self.assertEqual(data_list[0]['img_id'], 'P2805__1024__0___0')
        self.assertEqual(data_list[0]['file_name'], 'P2805__1024__0___0.png')
        self.assertEqual(data_list[0]['img_path'],
                         'tests/dota/data/images/P2805__1024__0___0.png')
        self.assertEqual(len(data_list[0]['instances']), 1)
        self.assertEqual(dataset.get_cat_ids(0), [[]])
