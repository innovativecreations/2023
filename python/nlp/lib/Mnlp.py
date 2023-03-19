import json

class Mnlp:
    listSen= []
    def __init__(self, sentences):
        self.listSen = sentences


    def tokenizer(self):
        with open("D:/2023/2023/python/nlp/lib/source/data.json") as d:
            dataOfWords = json.load(d)
        print(type(dataOfWords))
        for sentence in self.listSen:
            words = sentence.split(" ")
            print(list(dataOfWords.values()))
            for value in list(dataOfWords.values()):
                if not (value in words):
                    for i in words:
                        if i != value:
                            dataOfWords[len(dataOfWords)+1] = i
        with open("D:/2023/2023/python/nlp/lib/source/data.json", "w") as d:
            json.dump(dataOfWords, d)
        print(dataOfWords)

