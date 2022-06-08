#!/bin/bash
#$ -q gpu@@cvrl_gpu
#$ -l gpu_card=1
#$ -N magface

####################### Set Up ###############################

cd /afs/crc.nd.edu/user/p/ptinsley/magface/inference

module load cuda/11.6
nvcc --version

export PATH=/usr/local/cuda-11.6/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.6/lib64:$LD_LIBRARY_PATH

source ~/miniconda3/bin/activate magface
conda env list

module load gcc/

export CC=/opt/crc/g/gcc/8.3.0/bin/gcc
export CXX=/opt/crc/g/gcc/8.3.0/bin/g++

######################################################################

python gen_feat.py
# python gen_chips.py --i=$SGE_TASK_ID
