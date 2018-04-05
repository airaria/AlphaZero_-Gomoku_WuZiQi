BOARD_SIZE = (9,9)
BLACK = 1
WHITE = -1
C_PUCT = 2
N_SEARCH = 900
TEMPERATURE = 1.0

BATCH_SIZE = 64
MAX_SELF_PLAY = 5000
LEARNING_RATE = 0.0005
N_VIRTUAL_LOSS = 5
N_EVALUATE = 4
N_WORKER = 4 #4

BUFFER_SIZE = 20000
N_EPOCH_PER_TRAIN_STEP = 2
SELY_PLAY_PER_TRAIN = 2
SAVE_EVERY_N_EPOCH = 10
START_TRAIN_BUFFER_SIZE = 2500

SAVE_DIR = 'saved_model/'
LOAD_FN = None
MODE = "TRAIN" # 'TRAIN' or "TEST"
MAX_TO_KEEP = 20
