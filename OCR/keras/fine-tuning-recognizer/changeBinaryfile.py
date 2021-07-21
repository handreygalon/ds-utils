import pickle

from constant import *


with open(f'{GENERAL_FILES}/{DATASET_FILES}/gt.txt', "rb") as fp:   # Unpickling
    dataset = pickle.load(fp)

for i in range(len(dataset)):
    dataset[i] = list(dataset[i])  # Tuples are immutable. Convert to a list before processing.
    imgPath = dataset[i][0].split('/')[-1]
    dataset[i][0] = f'/content/drive/MyDrive/utils/keras_ocr/fine-tuning-recognizer/files/dataset/{imgPath}'
    dataset[i] = tuple(dataset[i])  # Now, back to a tuple

# print(f'Dataset:\n {dataset}')
with open(f'{GENERAL_FILES}/{DATASET_FILES}/gt_drive.txt', "wb") as fp:   #Pickling
    pickle.dump(dataset, fp)
