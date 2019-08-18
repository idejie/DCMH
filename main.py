import torch

import config
import yaml
import os
from utils.dataset import FlickrDataset
from PIL import Image
import numpy as np

if __name__ == '__main__':
    logger = config.get_logger()
    args = config.get_args()
    if args.action == 'train':
        # train
        logger.info('Arguments:%s' % args.__dict__)

        logger.info('======= start to load data ======')
        if args.config:
            logger.info('load file:\'%s\' as current configuration.' % args.config)
            try:
                with open(args.config) as f:
                    train_config = yaml.load(f, Loader=yaml.SafeLoader)
                # process data
                data_dir = train_config['data_dir']
                logger.info('loading dataset: \'%s\' from directory \'%s\'' % (train_config['data_set'], data_dir))
                if train_config['data_set'] == 'MIRFLICKR-25K':
                    image_dir = os.path.join(data_dir, 'images')
                    text_dir = os.path.join(data_dir, 'tags')
                    label_dir = os.path.join(data_dir, 'annotations')
                    flickr_dataset = FlickrDataset(image_dir, text_dir, label_dir)

                    width_max = 500
                    length_max = 500
                    for data in flickr_dataset:
                        image = Image.open(data['img'])
                        image = np.array(image)
                        image = torch.Tensor(image)
                        if image.size()[0] > width_max:
                            width_max = image.size()[0]
                        if image.size()[1] > length_max:
                            length_max = image.size()[1]
                        print(image.size())
                        break
                    print(width_max, length_max)

                elif train_config['data_set'] == 'IAPR TC-12':
                    pass
                elif train_config['data_set'] == 'NUS-WIDE':
                    pass
                else:
                    logger.error('not support this dataset: \'%s\'' % train_config['data_set'])
                    raise ValueError('not support this dataset: \'%s\'' % train_config['data_set'])
            except Exception as e:
                logger.error(e)
                raise e
        pass
    elif args.action == 'test':
        # test
        pass
    else:
        logger.error('no such action \'%s\'' % args.action)
        raise ValueError('no such action \'%s\'' % args.action)
