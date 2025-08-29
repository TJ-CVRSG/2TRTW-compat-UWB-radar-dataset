import os
import shutil
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


def split_data(dataset_path, val_volunteer, save_path):
    train_dir = os.path.join(save_path, 'train')
    val_dir = os.path.join(save_path, 'val')

    # 创建训练和验证目录
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)

    # 遍历主目录下的所有文件夹
    for folder_name in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder_name)
        if os.path.isdir(folder_path):
            volunteer_name = folder_name.split('_')[-1]
            if volunteer_name in val_volunteer:
                target_dir = val_dir
            else:
                target_dir = train_dir
            
            # 将数据复制到对应目录
            target_folder = os.path.join(target_dir, folder_name)
            if not os.path.exists(target_folder):
                shutil.copytree(folder_path, target_folder)

dataset_path = './all'
val_volunteer = ['Person4','Person9']
save_path = '/home/cvrsg/LRM/HAR/Dataset/Mydata/5cm_Person49val'
split_data(dataset_path, val_volunteer, save_path)

train_label_array = []
train_radar_array = []
val_label_array = []
val_radar_array = []

train_path = os.path.join(save_path,'train')
val_path = os.path.join(save_path,'val')

for list in os.listdir(train_path):
    index = -1
    bb_array = []

    while(list[index]!='_'):
        index-=1
    label = label_dict[list[:index]]
    preson_index = int(list[index+7:])
    for i in range(1,len(os.listdir(os.path.join(train_path, list)))+1):
        img_name = f'c{label}p{preson_index}n{i}.npy'
        img_path = os.path.join(train_path, list, img_name)

        train_label_array.append(label-1)
        train_radar_array.append(img_path)
        
for list in os.listdir(val_path):
    index = -1
    bb_array = []

    while(list[index]!='_'):
        index-=1
    label = label_dict[list[:index]]
    preson_index = int(list[index+7:])
    for i in range(1,len(os.listdir(os.path.join(val_path, list)))+1):
        img_name = f'c{label}p{preson_index}n{i}.npy'
        img_path = os.path.join(val_path, list, img_name)

        val_label_array.append(label-1)
        val_radar_array.append(img_path)
        
train_label_array = np.asarray(train_label_array)
train_radar_array = np.asarray(train_radar_array)
val_label_array = np.asarray(val_label_array)
val_radar_array = np.asarray(val_radar_array)

np.save(f'{save_path}/train_label_array.npy', train_label_array)
np.save(f'{save_path}/val_label_array.npy', val_label_array)
np.save(f'{save_path}/train_radar_array.npy', train_radar_array)
np.save(f'{save_path}/val_radar_array.npy', val_radar_array)