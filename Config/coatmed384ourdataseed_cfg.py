import sys
sys.path.append('./')
from paths import PATHS
import torch

class CFG:
    DDP = 1
    DDP_INIT_DONE = 0
    N_GPUS = 3
    FOLD = 3
    
    OUTPUT_FOLDER = f'{PATHS.MODEL_SAVE}/coatmed384ourdataseed'

    seed = 100
    
    device = torch.device('cuda')
    
    n_folds = 4
    folds = [i for i in range(n_folds)]
    
    # image_size = [320, 320]
    image_size = [384, 384]
    
    TAKE_FIRST = 96
    
    NC = 3

    train_batch_size = 1
    valid_batch_size = 2
    acc_steps = 2
    
    lr = 9e-5
    wd = 1e-6
    n_epochs = 12
    n_warmup_steps = 0
    upscale_steps = 1
    validate_every = 1
    
    epoch = 0
    global_step = 0
    literal_step = 0
    segw = 0.15
    autocast = True

    workers = 6