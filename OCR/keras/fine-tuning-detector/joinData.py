import numpy as np


class JoinData:
    def __init__(self, letters, boxPoints, folder, imgName, imgFormat):
        self.letters = letters
        self.boxPoints = boxPoints
        self.folder = folder
        self.imgName = imgName
        self.imgFormat = imgFormat
        self.joinBoxLetterTuple = ()
        self.joinBoxesLettersList = []
        self.joinBoxLetterList = []
        self.joinFilePath = ()
        self.dataset = []

    def callMe(self):
        # print(len(self.boxPoints))  # Quantidade de palavras
        # print(len(self.boxPoints[0]))  # Quantidade de letras da primeira palavra
        # print(self.boxPoints[0][0])  # Primeira caixa da primeira palavra
        # print(np.array(self.boxPoints[0][0]).reshape((4,2)))

        for i in range(len(self.boxPoints)):
            for j in range(len(self.boxPoints[i])):
                # print(self.boxPoints[i][j])
                # print(self.letters[i][j])
                self.joinBoxLetterTuple = (np.array(self.boxPoints[i][j]).reshape((4,2)), self.letters[i][j])
                self.joinBoxLetterList.append(self.joinBoxLetterTuple)
            self.joinBoxesLettersList.append(self.joinBoxLetterList)
            self.joinBoxLetterList = []

        # print(self.joinBoxesLettersList)

        self.joinFilePath = (
            f'{self.folder}/{self.imgName}.{self.imgFormat}', 
            self.joinBoxesLettersList, 
            1
        )

        # self.dataset.append(self.joinFilePath)
        # return self.dataset
        return self.joinFilePath
