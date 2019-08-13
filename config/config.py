import argparse
import logging


def get_args():
    parser = argparse.ArgumentParser(description='PyTorch implement for paper \'CVPR 2017 - Deep Cross-Modal Hashing\'')
    parser.add_argument('--action', '-a', type=str,
                        default='train', help='action choice between \'train\' or \'test\'')
    parser.add_argument('--train_data', type=str,
                        default='data/MIRFLICKR-25K', help='the data dir for train')
    parser.add_argument('--test_data', type=str,
                        default='data/MIRFLICKR-25K', help='the data dir for test')
    parser.add_argument('--epoch', '-e', type=int,
                        default=10, help='epoch of train')
    parser.add_argument('--batch_size', type=int,
                        default=50, help='batch size of train')
    args = parser.parse_args()
    return args


def get_logger():
    logger = logging.getLogger()
    return logger
