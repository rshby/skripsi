from typing import OrderedDict
import pandas as pd
import json

# fungsi yang digunakan untuk menampilkan df hasil hapus outlier
def showDfHapusOutlier():
    return pd.read_feather(r"C:\Users\ROG\Documents\skripsi\Datasets\df_hasil_hapus_outlier.feather").to_dict(orient="records")

# function yang digunakan untuk menampilkan dataframe X (features)
def showX():
    try:
        return pd.read_feather(r"C:\Users\ROG\Documents\skripsi\Datasets\X.feather").to_dict(orient="records")
    except Exception as e:
        print(f"kesalahan function showX: {e}")

# fucntion yang digunakan untuk menampilkan dataframe y (target)
def showY():
    try:
        return pd.read_csv(r"C:\Users\ROG\Documents\skripsi\Datasets\y.csv").to_dict(orient="records")
    except Exception as e:
        print(f"kesalahan function showY: {e}")

#function yang digunakan untuk menampilkan X_train
def showXtrain():
    try:
        return pd.read_feather(r"C:\Users\ROG\Documents\skripsi\Datasets\X_train.feather").to_dict(orient="records")
    except Exception as e:
        print(f"kesalahan function showXtrain: {e}")

# fucntion yang digunakan untuk menampilkan data X_train hasil scaling
def showXtrainScaling():
    try:
        return pd.read_feather(r"C:\Users\ROG\Documents\skripsi\Datasets\X_train_scaling.feather").to_dict(orient="records")
    except Exception as e:
        print(f"kesalahan function showXtrainScaling: {e}")

# function yang digunakan untuk menampilkan data X_train hasil onehot
def showXtrainOneHot():
    try:
        return pd.read_feather(r"C:\Users\ROG\Documents\skripsi\Datasets\X_train_onehot.feather").to_dict(orient="records")
    except Exception as e:
        print(f"kesalahan function showXtrainOneHot: {e}")

# function yang digunakan untuk menampilkan X_train hasil preprocessing
def showXtrainHasilPreprocessing():
    try:
        return pd.read_csv(r"C:\Users\ROG\Documents\skripsi\Datasets\X_train_hasil_preprocessing.csv").to_dict(orient="records")
    except Exception as e:
        print(f"kesalahan function showXtrainHasilPreprocessing: {e}")

# fucntion yang digunakan untuk menampilkan contoh data Training
def showContohDataTrain():
    try:
        return pd.read_feather(r"C:\Users\ROG\Documents\skripsi\Datasets\contoh_data_training.feather").to_dict(orient="records")
    except Exception as e:
        print(f"kesalahan function showContohDataTrain: {e}")