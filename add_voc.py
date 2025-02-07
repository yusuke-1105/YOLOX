# CVATで作成したPASCAL VOC datasetをYOLOXで使用するためのディレクトリ作成
# Create a directory to use the PASCAL VOC dataset created by CVAT in YOLOX.

import random
import sys

dir=f'{sys.argv[1]}/ImageSets/Main'
with open(f'{dir}/default.txt', 'r') as f:
    img_name = [s.strip() for s in f.readlines()]


num=len(img_name)   # 全画像数

train_num=int(num*0.75)         # 訓練画像数
val_num=int(num*0.20)           # 検証画像数
test_num=num-train_num-val_num  # テスト画像数

train_name: list = []
val_name: list = []
test_name: list = []

name=[train_name,val_name,test_name]

# ランダムに画像を選択し，`name`内のそれぞれのリストに格納
for i, each_num in enumerate([train_num, val_num, test_num]):
    for m in range(each_num):
        ran=random.randint(0,len(img_name)-1)
        name[i].append(img_name[ran])
        img_name.remove(img_name[ran])

with open(f'{dir}/train.txt', mode='w') as f:
    f.write('\n'.join(train_name))

with open(f'{dir}/test.txt', mode='w') as f:
    f.write('\n'.join(test_name))

with open(f'{dir}/val.txt', mode='w') as f:
    f.write('\n'.join(val_name))

with open(f'{dir}/trainval.txt', mode='w') as f:
    f.write('\n'.join(train_name))
    f.write('\n')
    f.write('\n'.join(val_name))

print("train size:", len(train_name))
print("test size", len(test_name))
print("val size:", len(val_name))
