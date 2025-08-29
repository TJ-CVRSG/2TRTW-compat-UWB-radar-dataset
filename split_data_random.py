import os
import numpy as np
label_dict = {'stand':1, 
              'forward':2, 
              'backward':3,
              'wave_hands':4,
              'bend':5,
              'crouch':6,
              'clap':7,
              'trun around':8,
              'jump':9}


label_array = []
radar_array = []

root_path = '/home/cvrsg/LRM/HAR/Dataset/Mydata/all_k100'

for list in os.listdir(root_path):
    index = -1
    bb_array = []
    if(len(list.split('.'))>1):
        continue
    while(list[index]!='_'):
        index-=1
    label = label_dict[list[:index]]
    preson_index = int(list[index+7:])
    for i in range(1,len(os.listdir(os.path.join(root_path, list)))+1):
        img_name = f'c{label}p{preson_index}n{i}.npy'
        img_path = os.path.join(root_path, list, img_name)

        label_array.append(label-1)
        radar_array.append(img_path)
        
label_array = np.asarray(label_array)
radar_array = np.asarray(radar_array)

def shuffle_data(img_array, label_array, seed=None):

    # 确保两个数组的第一个维度相同
    assert len(img_array) == len(label_array), "img_array 和 label_array 的长度必须相同"
    # 设置随机种子
    if seed is not None:
        np.random.seed(seed)
    # 生成随机排列的索引
    permutation = np.random.permutation(len(img_array))
    # 打乱数组
    shuffled_img_array = img_array[permutation]
    shuffled_label_array = label_array[permutation]
    return shuffled_img_array, shuffled_label_array

def split_data(img_array, label_array, train_ratio=0.9, seed=66):
    # 打乱数据
    shuffled_img_array, shuffled_label_array = shuffle_data(img_array, label_array, seed)
    # 计算训练集大小
    train_size = int(len(shuffled_img_array) * train_ratio)
    # 分割数据集
    train_img_set = shuffled_img_array[:train_size]
    test_img_set = shuffled_img_array[train_size:]
    train_label_set = shuffled_label_array[:train_size]
    test_label_set = shuffled_label_array[train_size:]
    
    return train_img_set, test_img_set, train_label_set, test_label_set

train_radar_array, val_radar_array, train_label_array, val_label_array = split_data(radar_array, label_array)


np.save(f'{root_path}/train_label_array.npy', train_label_array)
np.save(f'{root_path}/val_label_array.npy', val_label_array)
np.save(f'{root_path}/train_radar_array.npy', train_radar_array)
np.save(f'{root_path}/val_radar_array.npy', val_radar_array)