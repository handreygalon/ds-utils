import pickle

from constant import *


with open(f'{GENERAL_FILES}/boxes_txt/nf-1.txt', "rb") as fp:   # Unpickling
    dataset = pickle.load(fp)    
print(dataset)
