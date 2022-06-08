import os, glob
from PIL import Image

# import random

import torch
import argparse
from facenet_pytorch import MTCNN

fnames = glob.glob('./MPIE/**/**/*.png')

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--i', type=int, required=True,
                    help='an integer')
args = parser.parse_args()

# with open('./MPIE/img.list','w') as f:
#     for fname in fnames:
#         f.write('{}\n'.format(fname))

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))

mtcnn = MTCNN(image_size=112, device=device)

i = args.i

# print(i)

for fname in fnames[10955*i:10955*(i+1)]:
    img = Image.open(fname)
    img_cropped = mtcnn(img, save_path='/scratch365/ptinsley/MPIE_chips/{}'.format(fname.split('/')[-1]))