#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:40:50 2018

@author: ubuntu

这个config文件模板参考mmcv
"""

import sys

"""--------------------model-------------------------------
用于定义模型相关参数，如下是相关必选参数，不可修改变量名
model
"""
model_name = 'LeNet5'

"""--------------------datasets-------------------------------
用于定义数据集相关参数，如下是相关必选参数，不可修改变量名
dataset_name/data_root/mean/std/num_classes/input_size/input_layers/batch_size
"""
dataset_name = 'cifar10'       # 如果是exist_datasets则需要输入跟exist_datasets要求的名字
if sys.platform == 'linux':    # for ubuntu
    data_root = '/home/ubuntu/MyDatasets/CIFAR10'     # for ubuntu 
else:                          # for Mac os
    data_root = '/Users/suliang/MyDatasets/CIFAR10'   # for mac os
mean = [0.4914, 0.4822, 0.4465]
std = [0.2023, 0.1994, 0.2010]
num_classes = 10
input_size = 32   # 图片传入网络的size: 不同model对input_size要求不同(lenet=32, alexnet/vgg/resnet=224)
input_layers = 3  # 图片传入网络的层数: 灰度图为1, RGB图为3
batch_size = 64

"""--------------------optimizer-------------------------------
用于优化器相关参数，如下是相关必选参数，不可修改变量名
optimizer
可定义为字典optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=5e-4)
也可定义为对象optimizer = torch.optim.SGD()
"""
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=5e-4)

"""--------------------runtime-------------------------------
运行时相关参数，如下是相关必选参数，不可修改变量名
epoch_num/
"""
epoch_num = 7
checkpoints_dir = '../checkpoints'
working_dir = '../checkpoints/working'   # 在checkpoints目录下添加一个输出工作文件夹
gpus = range(2)   # 1表示单GPU，>=2表示DataParallel, 0表示cpu
dist_params = dict(backend='nccl')
data_workers = 2  # data workers per gpu
workflow = [('train', 1), ('val', 1)]
#resume_from = '../checkpoints/LeNet5_epoch_6.pth'
resume_from = None
load_from = None
topk = 2

"""--------------------hooks config-------------------------------
用于所有hooks的config，如下是相关比选hook config，不可修改变量名
optimizer_config/log_config/
"""
optimizer_config = dict(
    grad_clip=None)
lr_config = dict(
    policy='step', 
    step=2)
checkpoint_config = dict(
    interval=1, 
    save_optimizer=True, 
    out_dir=checkpoints_dir)  # -1表示不保存，n次/epoch
logger_config = dict(
    interval=20, 
    ignore_last=True, 
    logs = ['LoggerTextHook','LoggerVisdomHook'])  # ignore_last=False则强制在epoch最后一个iter计算一次
cache_config = dict(
    before_epoch=False,
    after_epoch=True,      # 在每个epoch结束后清除cuda cache
    after_iter=False)



