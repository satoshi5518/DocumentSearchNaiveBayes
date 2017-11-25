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
fc.importTrainingDocFile(r'.\TrainingData\*_*.txt')
# for traingData in fc.trainingDataList:
#     for data in traingData:
#         print(data)

# ナイーブベイズ分類器を訓練
nb = NaiveBayes()
nb.train(fc.trainingDataList)
# for category in nb.categories:
#     for vocabulary in nb.vocabularies:
#         print("( category->" + category + " vocabularies->" + vocabulary + " ) " + str(nb.wordProb(vocabulary,category)))

# 学習データの生成
# fc.exportLearningArrayCSV("categories.csv",nb.categories) # カテゴリの集合
# fc.exportLearningArrayCSV("vocabularies.csv",nb.vocabularies) # ボキャブラリの集合
# fc.exportLearningAssArrayListCSV("wordcount.csv",nb.wordcount) # カテゴリでの単語の出現回数
# fc.exportLearningAssArrayCSV("catcount.csv",nb.catcount) # カテゴリの出現回数
# fc.exportLearningAssArrayCSV("denominator.csv",nb.denominator) # P(word|cat)の分母の値

# print(nb.categories)
# print(nb.vocabularies)
# print(nb.wordcount)
# print(nb.catcount)
# print(nb.denominator)

# 学習データの読み込み
# nb.categories = fc.importLearningArrayCSV("categories.csv") # カテゴリの集合
# nb.vocabularies = fc.importLearningArrayCSV("vocabularies.csv") # ボキャブラリの集合
# nb.wordcount = fc.importLearningAssArrayListCSV("wordcount.csv") # カテゴリでの単語の出現回数
# nb.catcount = fc.importLearningAssArrayCSV("catcount.csv") # カテゴリの出現回数
# nb.denominator = fc.importLearningAssArrayCSV("denominator.csv") # P(word|cat)の分母の値

# print(nb.categories)
# print(nb.vocabularies)
# print(nb.wordcount)
# print(nb.catcount)
# print(nb.denominator)

for category in nb.categories:
    test = fc.importTestDocFile(r'.\TestData\餃子_TEST0001.txt')
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
