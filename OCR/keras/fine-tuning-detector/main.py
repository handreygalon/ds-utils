import pickle

from constant import *
from boxMaker import BoxMaker
from splitWords import SplitWords
from joinData import JoinData


if __name__ == '__main__':
    imgName = 'nf-1'
    filename = f'{imgName}_palavras'
    letters = []
    boxPoints = []
    
    splitWord = SplitWords()
    letters = splitWord.callMe(GENERAL_FILES, filename)
    
    box = BoxMaker(GENERAL_FILES, imgName, IMG_FORMAT)
    boxPoints = box.callMe()
    
    joinFinal = JoinData(letters, boxPoints, GENERAL_FILES, imgName, IMG_FORMAT)
    dataset = joinFinal.callMe()

    # file = open(f'{GENERAL_FILES}/{imgName}.txt', 'w')
    # file.write("{}".format(dataset))
    # file.close()

    with open(f'{GENERAL_FILES}/{BOX_TEXT_FILES}/{imgName}.txt', "wb") as fp:   #Pickling
        pickle.dump(dataset, fp)

    # with open(f'{GENERAL_FILES}/{BOX_TEXT_FILES}/{imgName}.txt', "rb") as fp:   # Unpickling
    #     b = pickle.load(fp)
