# -*- coding: utf-8 -*-
import FileController
from FileController import FileController
import NaiveBayes
from NaiveBayes import NaiveBayes

########## メイン処理 ##########
print('メイン処理開始')

# 訓練データの読み込み
fc = FileController()
fc.importTrainingFile(r'.\TrainingData\*_*.txt')
# for traingData in fc.trainingDataList:
#     for data in traingData:
#         print(data)


# ナイーブベイズ分類器を訓練
nb = NaiveBayes()
nb.train(fc.trainingDataList)
for category in nb.categories:
    for vocabulary in nb.vocabularies:
        print("( category->" + category + " vocabularies->" + vocabulary + " ) " + str(nb.word_probability(vocabulary,category)))

for category in nb.categories:
    test = fc.importTestFile(r'.\TestData\餃子_TEST0001.txt')
    print("log P(" + category + "|test) = ",nb.score(test,category))

