import os

from .output import Output
from ..util.logger import Logger


class Trainer(Output):
    def __init__(self, session_name):
        dir_list = ["checkpoint", "img", "tboard"]
        Output.__init__(session_name, dir_list)
        
        self.logger = Logger()

    def train(self):
        pass

    def train_epoch(self):
        pass

    def train_step(self):
        pass

    def warmup(self):
        pass

    def before_train(self):
        pass

    def after_train(self):
        pass

    def before_step(self):
        pass

    def after_step(self):
        pass

    def save_checkpoint(self):
        # torch.save({'epoch': self.epoch+1,
        #             'model_weight': self.model.module.state_dict(),
        #             'optimizer': self.optimizer},
        #             path.join(self.config['train']['checkpoint_dir'], self.checkpoint_name))
        raise NotImplementedError

    def load_checkpoint(self):
        # saved_checkpoint = torch.load(file_name)
        # self.epoch = saved_checkpoint['epoch']
        # self.model.module.load_state_dict(saved_checkpoint['model_weight'])
        # self.optimizer = saved_checkpoint['optimizer']
        raise NotImplementedError
