import pandas as pd


class SplitWords:
    def __init__(self):
        self.data = []

    def split(self, word): 
        return [char for char in word]  

    def callMe(self, folder, filename):
        content = pd.read_csv(f'{folder}/{filename}.txt', header=None)
        letters, words = [], [] 

        for i in range(len(content)):
            word = content[0][i].replace(' ', '')
            words.append(word)

        for i in range(len(words)):
            letters.append(self.split(words[i]))
        
        return letters

    
