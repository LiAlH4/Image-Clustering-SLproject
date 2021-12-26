#!/bin/bash
#SBATCH -J test
#SBATCH --qos=short

#SBATCH --cpus-per-task=4     # 申请 4 cpu
#SBATCH --gres=gpu:1          # 申请 1 gpu
#SBATCH -N 1
#SBATCH -t 1-00:00:00
#SBATCH --mem=10G

module add anaconda cuda/10.0
source activate SCAN_env

python simclr.py --config_env configs/env.yml --config_exp configs/pretext/simclr_mnist.yml
python scan.py --config_env configs/env.yml --config_exp configs/scan/scan_mnist.yml
python selflabel.py --config_env configs/env.yml --config_exp configs/selflabel/selflabel_mnist.yml