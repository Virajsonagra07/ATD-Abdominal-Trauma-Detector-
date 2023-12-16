import sys
sys.path.append('./')
from paths import PATHS
import torch

class CFG:
    DDP = 1
    DDP_INIT_DONE = 0
    N_GPUS = 3
    FOLD = 3
    
    OUTPUT_FOLDER = f'{PATHS.MODEL_SAVE}/coatmed384_v3nc_exp2_384_diffseg5'
    

    seed = 3407
    
    device = torch.device('cuda')
    
    n_folds = 4
    folds = [i for i in range(n_folds)]
    
    #image_size = [128, 128]
    image_size = [384, 384]
    
    TAKE_FIRST = 96
    
    NC = 3

    train_batch_size = 1
    valid_batch_size = 2
    acc_steps = 2
    
    lr = 1e-4
    wd = 1e-6
    n_epochs = 11
    n_warmup_steps = 0
    upscale_steps = 1
    validate_every = 1
    
    epoch = 0
    global_step = 0
    literal_step = 0

    autocast = True

    workers = 6