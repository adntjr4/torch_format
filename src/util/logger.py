import threading
import logging, time, os

from .progress_msg import ProgressMsg
from .chart import LossChart


class Logger(ProgressMsg):
    def __init__(self, session_name:str, max_iter:tuple, log_dir:str=None, log_lvl:str='info', log_include_time:bool=False):
        '''
        Args:
            session_name (str)
            max_iter (tuple) : max iteration for progress
            log_dir (str) : if None, no file out for logging
            log_lvl (str) : 'debug', 'info'
            log_include_time (bool)
        '''
        assert log_lvl in ['debug', 'info']

        # init progress message class
        ProgressMsg.__init__(self, max_iter)

        # log setting
        self.log_dir = log_dir
        self.logging_lvl = logging.INFO if log_lvl=='info' else logging.DEBUG
        self.log_include_time = log_include_time

        # set configs
        self.set_cfg()
        
        # init logging
        logging.basicConfig(
            format=self.logging_format,
            level=self.logging_lvl,
            handlers=self.logging_handler
            )

        self.session_name = session_name

    def set_cfg(self):
        self.logging_mode = 'w' # 'a': add, 'w': over write

        # logging format
        if self.log_include_time:
            self.logging_format = '[%(asctime)s] %(message)s'
        else:
            self.logging_format = '%(message)s'

        # logging handler
        self.logging_handler = [logging.StreamHandler()]
        if self.log_dir is not None: self.logging_handler.append(logging.FileHandler(filename=self.log_dir, mode=self.logging_mode))

    def set_log_lvl(self, log_lvl):
        self.logging_lvl = logging.INFO if log_lvl=='info' else logging.DEBUG
        logging.basicConfig(
            format=self.logging_format,
            level=self.logging_lvl,
            handlers=self.logging_handler
            )

    def debug(self, txt):
        self.p_msg.line_reset()
        logging.debug(txt)

    def info(self, txt):
        self.p_msg.line_reset()
        logging.info(txt)

    def clear_screen(self):
        if os.name == 'nt': 
            os.system('cls') 
        else: 
            os.system('clear') 


# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
# currently not using
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
