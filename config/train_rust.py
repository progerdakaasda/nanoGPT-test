out_dir = 'out-rust'

dataset = 'rust'


eval_interval = 50
eval_iters = 100
log_interval = 10

always_save_checkpoint = True


# model
n_layer = 12
n_head = 12
n_embd = 768

block_size = 512

dropout = 0.0
bias = False


# training
batch_size = 14
gradient_accumulation_steps = 8

max_iters = 200000


learning_rate = 3e-4
min_lr = 3e-5

warmup_iters = 2000

weight_decay = 0.1

beta1 = 0.9
beta2 = 0.95


compile = True
