from configs import config
import yaml
import os

logger = config.get_logger()
if __name__ == '__main__':
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

            except Exception as e:
                logger.error(e)
                raise e
        pass
    elif args.action == 'test':
        # test
        pass
    else:

        raise ValueError('no such action \'%s\'' % args.action)
