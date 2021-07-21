import pickle
import glob

from constant import *


if __name__ == '__main__':
    kerasDataset = []

    for filename in glob.glob(f'{GENERAL_FILES}/{BOX_TEXT_FILES}/*.txt'):
        name = filename.split('\\')[-1]
        with open(f'{GENERAL_FILES}/{BOX_TEXT_FILES}/{name}', "rb") as fp:   # Unpickling
            b = pickle.load(fp)
            kerasDataset.append(b)
    
    # print(kerasDataset)

    with open(f'{GENERAL_FILES}/keras_ocr_dataset.txt', "wb") as fp:   #Pickling
        pickle.dump(kerasDataset, fp)

    with open(f'{GENERAL_FILES}/keras_ocr_dataset.txt', "rb") as fp:   # Unpickling
        b = pickle.load(fp)    
    print(f'FIM: {b}')
        