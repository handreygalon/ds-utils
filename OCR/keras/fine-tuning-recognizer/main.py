import pickle

from constant import *
from cropWord import CropWord


if __name__ == '__main__':
    imgName = 'nf-10'

    words = CropWord(GENERAL_FILES, DATASET_FILES, imgName, IMG_FORMAT)
    dataset = words.callMe()
    
    # file = open(f'{GENERAL_FILES}/dataset.txt', 'w')
    # file.write(f'{dataset}')
    # file.close()

    with open(f'{GENERAL_FILES}/{DATASET_FILES}/{imgName}.txt', "wb") as fp:   #Pickling
        pickle.dump(dataset, fp)
    # with open(f'{GENERAL_FILES}/{BOX_TEXT_FILES}/{imgName}.txt', "rb") as fp:   # Unpickling
    #     b = pickle.load(fp)
