import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.util.logger import Logger

import time, os, random

lg = Logger(session_name='Logger test', max_iter=(10, 10), log_dir='log.log')

lg.start((0,0))

for i in range(10):
    for j in range(10):
        data = 2**(1/(i*100+j+10))+random.random()/100
        time.sleep(0.1)
