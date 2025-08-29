# 2TRTW-compat-UWB-radar-dataset for "Through-Wall Human Activity Recognition with Compact MIMO Ultra-Wideband Radar" 

## 📂 Dataset Description

The dataset was collected for the task of Through-Wall Human Activity Recognition using compact MIMO UWB radar system. It includes:

- **Sensor type**: [MIMO UWB Radar]
- **Sampling rate**: [23.328 GHz pulse repetition]
- **Data format**: [.npy]
- **Environments**: [unobstructed, glass door, concrete wall, wooden wall]
- **Feature types**: [Time-Range (TR)]

See [`dataset/README.md`](dataset/README.md) for full details on folder structure, file naming, and preprocessing methods.

---

## Name Rule
In the raw data folder,each sequence radar data is named like:c3p0n1
c means class
p means people
n means repeat times

## 🛠️ How to Use
1. download the raw data
https://drive.google.com/file/d/1fRv8orun9h5AmGQn2Yi69cHyKL0ZiOD7/view?usp=sharing
2. split the data
you can use the scripts to split data in random way or with LOSO method.
