import torch

from src.



def main(config):
    pass


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-c', '--config', default=None, type=str)
    args.add_argument('-d', '--device', default=None, type=str)
    args.add_argument('-r', '--resume', action='store_true')

    args = args.parse_args()

    assert args.config is not None, 'config file path is needed'
    assert args.device is not None, 'config file path is needed'

    config = ConfigParser(args)

    main(config)
