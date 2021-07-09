import pickle

from boxMaker import BoxMaker
from splitWords import SplitWords
from joinData import JoinData


if __name__ == '__main__':
    folder = 'files'
    imgFormat = 'jpg'      # jpeg     jpg    png
    imgName = '295'
    filename = f'{imgName}_palavras'
    letters = []
    boxPoints = []
    
    splitWord = SplitWords()
    letters = splitWord.callMe(folder, filename)
    
    box = BoxMaker(folder, imgName, imgFormat)
    boxPoints = box.callMe()
    ''' 
    letters = [
        ['D', 'a'], 
        ['d', 'o']
    ]
    boxPoints = [
        [
            [(198, 172), (196, 210), (221, 213), (222, 175)], 
            [(241, 177), (245, 213), (268, 214), (267, 184)]
        ], 
        [
            [(287, 233), (289, 271), (316, 271), (317, 235)], 
            [(340, 237), (341, 267), (362, 269), (363, 242)]
        ]
    ]
    '''

    joinFinal = JoinData(letters, boxPoints, folder, imgName, imgFormat)
    dataset = joinFinal.callMe()

    # file = open(f'{folder}/{imgName}.txt', 'w')
    # file.write("{}".format(dataset))
    # file.close()
    with open(f'{folder}/{imgName}.txt', "wb") as fp:   #Pickling
        pickle.dump(dataset, fp)

    with open(f'{folder}/{imgName}.txt', "rb") as fp:   # Unpickling
        b = pickle.load(fp)

    print(type(b[0][1][0][0][0]))
    print(b[0][1][0][0][0])

