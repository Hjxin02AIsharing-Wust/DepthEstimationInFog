from __future__ import absolute_import, division, print_function

import time

from trainer import Trainer
from options import MonodepthOptions

options = MonodepthOptions()
opts = options.parse()


if __name__ == "__main__":
    start = time.perf_counter()
    trainer = Trainer(opts)
    trainer.train()
    end = time.perf_counter()
    print('运行耗时', end - start)
