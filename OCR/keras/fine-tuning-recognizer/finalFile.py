import pickle
import glob

from constant import *


if __name__ == '__main__':
    segmentedDataset = []
    kerasDataset = []

    for filename in glob.glob(f'{GENERAL_FILES}/{DATASET_FILES}/*.txt'):
        name = filename.split('\\')[-1]
        with open(f'{GENERAL_FILES}/{DATASET_FILES}/{name}', "rb") as fp:   # Unpickling
            dataset = pickle.load(fp)
            segmentedDataset.append(dataset)
    
    for dataset in segmentedDataset:
        for i in range(len(dataset)):
            kerasDataset.append(dataset[i])

    # print(kerasDataset)

    with open(f'{GENERAL_FILES}/{DATASET_FILES}/gt.txt', "wb") as fp:   #Pickling
        pickle.dump(kerasDataset, fp)

    # with open(f'{GENERAL_FILES}/{DATASET_FILES}/gt.txt', "rb") as fp:   # Unpickling
    #     res = pickle.load(fp)    
    # print(f'FIM: {res}')
