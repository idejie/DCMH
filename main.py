from config import config

if __name__ == '__main__':
    args = config.get_args()
    if args.action == 'train':
        # train
        print('train')
        pass
    elif args.action == 'test':
        # test
        pass
    else:
        raise ValueError('no such action \'%s\'' % args.action)
