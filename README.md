# AlphaZero_Gomoku_WuZiQi

## 目前状态

结束第八次实验，训练到了680th generation，总计对弈约两万局，性能出现退化。
目前最佳模型约出现在第八次实验的400th generation~540th generation范围。

##  config.py 配置

一些参数说明：

- BOARD_SIZE : 棋盘大小。
- C_PUCT : 探索程度控制，参见AlphaGo Zero原文。
- N_SEARCH ：每走一步执行多少次局面求值。
- TEMPERATURE：走子随机化程度控制，参见AlphaGo Zero原文。
- MAX_SELF_PLAY：每个进程的总对局数。
- N_VIRTUAL_LOSS：virtual_loss大小，参见AlphaGo原文。
- N_EVALUATE：每次探索N_EVALUATE个叶子节点，再统一计算这些节点的value。此值>1时，请保证N_VIRTUAL_LOSS > 0。
- N_WORKER：并行self-play的进程数。**每步的探索次数=N_WORKER * N_SEARCH * N_EVALUATE** 。
- BUFFER_SIZE：储存对弈局面的buffer大小。
- N_EPOCH_PER_TRAIN_STEP：每次训练时，在已收集的self-play数据上过几个epoch。
- SELF_PLAY_PER_TRAIN：每次训练前，每个进程self-play的局数。
- SAVE_EVERY_N_EPOCH：顾名思义。
- START_TRAIN_BUFFER_SIZE：buffer中至少收集到这么多数据时才开始训练。
- SAVE_DIR：模型保存目录
- LOAD_FN：待加载模型文件，值为文件名或None。
- MODE：
  - 等于 "TRAIN" 时：如果LOAD_FN不是None ，那么加载模型文件并训练；否则从头训练。
  - 等于 "TEST" 时，如果LOAD_FN不是None，那么加载模型文件并进入人机对战模式；否则随机初始化模型并对战。
  - 等于 ”EVAL"时，读入模型文件P1和P2，P1执黑先行，进行对弈。
- MAX_TO_KEEP：最多保存多少个模型文件。

请根据实际的计算资源调整配置。

## 编译动态库

gcc -shared -fPIC  arb.c -o libarb.so

## 训练

python main.py

## 人机对战

python main.py  

输入格式为 

x,y

## 模型对战

python main.py

## 已知问题

1. ~~尚未实现自我对弈的模型评测。~~
2. ~~输入格式错误时直接退出。~~
3. 胜率预测非常不靠谱，或许是网络太小，容量不够?

## TODO
1. ~~上传训练完成的模型~~
2. ~~将模型文件从PyTorch迁移到Caffe2~~
3. Pytorch 0.4 compatibility.

## Acknowledgements

参考了以下实现：

minigo: https://github.com/tensorflow/minigo

AlphaZero_Gomoku : https://github.com/junxiaosong/AlphaZero_Gomoku
