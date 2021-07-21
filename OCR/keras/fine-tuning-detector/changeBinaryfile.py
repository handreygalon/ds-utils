import pickle

from constant import *


with open(f'files/keras_ocr_dataset.txt', "rb") as fp:   # Unpickling
    dataset = pickle.load(fp)    

for i in range(len(dataset)):
    dataset[i] = list(dataset[i])  # Tuples are immutable. Convert to a list before processing.
    imgPath = dataset[i][0].split('/')[1]
    dataset[i][0] = f'/content/drive/MyDrive/keras-ocr-box-maker/files/{imgPath}'
    dataset[i] = tuple(dataset[i])  # Now, back to a tuple

# print(f'Dataset:\n {dataset}')
with open(f'{GENERAL_FILES}/keras_ocr_dataset_drive.txt', "wb") as fp:   #Pickling
    pickle.dump(dataset, fp)
