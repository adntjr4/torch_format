import os

from .output import Output
from ..dataset.custom_dataset import CustomDataSet
from ..util.logger import Logger
from ..util.warmup_scheduler import WarmupLRScheduler


class Trainer(Output):
    def __init__(self, cfg):
        self.session_name = cfg['session_name']

        self.checkpoint_folder = 'checkpoint'

        dir_list = ['checkpoint', 'img', 'tboard']
        Output.__init__(self.session_name, dir_list)
        
        self.logger = Logger()

        self.cfg = cfg

    def test(self):
        pass

    def train(self):
        self._before_train()

        # warmup
        if self.epoch == 0 and self.cfg.resume:
            self._warmup()

        # training
        for self.epoch in range(self.epoch, self.max_epoch):
            self._before_epoch()
            self._run_epoch()
            self._after_epoch()
        
        self._after_train()

    def _warmup(self):
        self.status = 'warmup'

        warmup_iter = self.cfg['training']['warmup_iter']
        self.scheduler = WarmupLRScheduler(self.optimizer)

        for self.iter in range(warmup_iter):
            self._before_step()
            self._run_step()
            self._after_step()

        
        pass

    def _run_epoch(self):
        for self.iter in range(self.max_iter):
            self._before_step()
            self._run_step()
            self._after_step()

    def _run_step(self):
        # get data

        # to device

        # get losses

        # backward

    

    def _before_train(self):
        # initialing message
        self.logger.info("initialing train setup...")

        # initialing
        self.model = 
        self.data_set = 
        self.data_loader = 
        self.epoch = self.start_epoch = 0
        self.max_epoch = 

        # resume
        if self.cfg["resume"]:
            # find last checkpoint
            checkpoint_name = self.session_name + str(self.epoch+1) + '.pth'
            load_epoch = find_last_epoch()

            # load last checkpoint
            self.load_checkpoint(load_epoch)

        # start message
        self.logger.info("training start")

    def _after_train(self):
        # finish message
        self.logger.info("training finish")

    def _before_epoch(self):
        self.status = 'epoch %02d/%02d'%(self.epoch, self.max_epoch)

        self._data_loader_iter = iter(self.data_loader)
        self.max_iter = self.data_loader.dataset.__len__()

    def _after_epoch(self):
        # save checkpoint
        self.save_checkpoint()

        # validation
        if self.cfg['validation']['val']:
            # do validation

    def _before_step(self):
        pass

    def _after_step(self):
        # print loss
        if self.iter % self.cfg['log']['interval_iter'] == 0:
            self.print_loss()

        # print progress
        self.logger.print_prog_msg((self.epoch, self.iter))

    def print_loss(self):
        loss_out_str = '[%s] %04d/%04d - '%(self.status, self.iter, self.max_iter)
        for loss_name in self.loss_dict:
            loss_out_str += '%s : %.4f | '%(loss_name, self.loss_dict[loss_name]/self.cfg['log']['interval_iter'])
            self.loss_dict[loss_name] = 0.
        self.logger.info(loss_out_str)

    def save_checkpoint(self):
        checkpoint_name = self.session_name + str(self.epoch+1) + '.pth'
        torch.save({'epoch': self.epoch+1,
                    'model_weight': self.model.module.state_dict(),
                    'optimizer': self.optimizer},
                    path.join(self.get_dir(self.checkpoint_folder), checkpoint_name))

    def load_checkpoint(self, load_epoch):
        saved_checkpoint = torch.load(file_name)
        self.epoch = saved_checkpoint['epoch']
        self.model.module.load_state_dict(saved_checkpoint['model_weight'])
        self.optimizer = saved_checkpoint['optimizer']

    def _find_last_epoch(self):
        checkpoint_list = os.listdir(self.get_dir(self.checkpoint_folder))
        epochs = [int(ckpt.replace('%s'%self.session_name, '').replace('.pth', '')) for ckpt in checkpoint_list]
        return max(epochs)
