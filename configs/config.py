import argparse
import logging
import logging.config
import os
from yaml import load, SafeLoader

LOGGING_CONF = 'configs/logging.yaml'
LOGGING_DIR = 'logging'


def get_args():
    parser = argparse.ArgumentParser(description='PyTorch implement for paper \'CVPR 2017 - Deep Cross-Modal Hashing\'')
    parser.add_argument('--action', '-a', type=str,
                        default='train', help='choice between \'train\' or \'test\' for action')
    parser.add_argument('--epoch', '-e', type=int,
                        default=10, help='epoch of train')
    parser.add_argument('--batch_size', type=int,
                        default=50, help='batch size of train')
    parser.add_argument('--config', '-c', type=str,
                        help='the configuration file')
    args = parser.parse_args()
    return args


def get_logger():
    if not os.path.exists(LOGGING_DIR):
        os.mkdir(LOGGING_DIR)
    os.makedirs(LOGGING_DIR, exist_ok=True)
    if not os.path.exists(LOGGING_CONF):
        logging.basicConfig(level=logging.WARNING,
                            format='%(asctime)s  %(filename)s[line:%(lineno)d] - %(levelname)s:  %(message)s')

        logger = logging.getLogger(__name__)
        logger.warning('No logging configuration file, use the default configuration.')
    else:
        with open(LOGGING_CONF) as f:
            config = load(f, Loader=SafeLoader)
        logging.config.dictConfig(config)
        logger = logging.getLogger(__name__)
    return logger
