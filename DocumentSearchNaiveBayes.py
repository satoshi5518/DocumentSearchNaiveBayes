# -*- coding: utf-8 -*-
# 参考HP http://aidiary.hatenablog.com/entry/20100613/1276389337

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
        print("( category->" + category + " vocabularies->" + vocabulary + " ) " + str(nb.wordProb(vocabulary,category)))

for category in nb.categories:
    test = fc.importTestFile(r'.\TestData\餃子_TEST0001.txt')
    print("log P(" + category + "|test) = ",nb.score(test,category))
print(nb.classify(test))

# data = [["yes", "Chinese", "Beijing", "Chinese"],
#         ["yes", "Chinese", "Chinese", "Shanghai"],
#         ["yes", "Chinese", "Macao"],
#         ["no", "Tokyo", "Japan", "Chinese"]]

# # ナイーブベイズ分類器を訓練
# nb = NaiveBayes()
# nb.train(data)

# print("P(Chinese|yes) = ", nb.wordProb("Chinese", "yes"))
# print("P(Tokyo|yes) = ", nb.wordProb("Tokyo", "yes"))
# print("P(Japan|yes) = ", nb.wordProb("Japan", "yes"))
# print("P(Chinese|no) = ", nb.wordProb("Chinese", "no"))
# print("P(Tokyo|no) = ", nb.wordProb("Tokyo", "no"))
# print("P(Japan|no) = ", nb.wordProb("Japan", "no"))
# #
# # # テストデータのカテゴリを予測
# test = ["Chinese", "Chinese", "Chinese", "Tokyo", "Japan"]
# print("log P(yes|test) =", nb.score(test, "yes"))
# print("log P(no|test) =", nb.score(test, "no"))
# print(nb.classify(test))
