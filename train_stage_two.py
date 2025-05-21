from __future__ import absolute_import, division, print_function

from trainer_stage_two import Trainer
from options import MonodepthOptions
from reproducibility import set_seed

options = MonodepthOptions()
opts = options.parse()


if __name__ == "__main__":
    # Fix random seed
    seed = 42
    set_seed(seed)

    trainer = Trainer(opts)
    trainer.train()
