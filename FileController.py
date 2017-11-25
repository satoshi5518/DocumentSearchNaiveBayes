# -*- coding: utf-8 -*-
import glob
import re
import csv
from janome.tokenizer import Tokenizer
from collections import defaultdict

# ファイル操作クラス
class FileController:

    ########## 初期処理 ##########
    def __init__(self) :
        print("初期処理")
        self.trainingDataList = []

    ########## 訓練データ読み込み処理 ##########
    # ファイルを["タグ","名詞","名詞"・・・]フォーマットの多次元配列に変換する。
    def importTrainingDocFile(self,path = "") :

        # フォルダーにあるすべてのファイルを取得
        files = glob.glob(path)
        t = Tokenizer()

        for file in files:
            trainingData = []
            tag = re.search(r'_.*?_',file).group().replace('_','')
            trainingData.append(tag)
            
            for line in open(file,'r',encoding="utf-8"):
                for token in t.tokenize(line):
                    if token.part_of_speech.split(',')[0] == "名詞" and token.part_of_speech.split(',')[1] == "一般":
                        trainingData.append(token.surface)
            
            self.trainingDataList.append(trainingData)

    ########## 訓練データ読み込み処理 ##########
    # ファイルを["タグ","名詞","名詞"・・・]フォーマットの多次元配列に変換する。
    def importTestDocFile(self,path = "") :
        testData = []
        t = Tokenizer()
        for line in open(path,'r',encoding="utf-8"):
            for token in t.tokenize(line):
                if token.part_of_speech.split(',')[0] == "名詞" and token.part_of_speech.split(',')[1] == "一般":
                    testData.append(token.surface)
            
        return testData

    ########## 学習データ書き出し処理(2次元配列用) ##########
    def exportLearningArrayListCSV(self,fileName = "",dataArrayList = []) :
        filepath = '.\\LearningData\\' + fileName
        f = open(filepath, 'w') 
        for dataArray in dataArrayList:
            f.writelines(",".join(map(str, dataArray)))
            f.write('\n')
        f.close()

    ########## 学習データ書き出し処理(1次元配列用) ##########
    def exportLearningArrayCSV(self,fileName = "",dataArray = []) :
        filepath = '.\\LearningData\\' + fileName
        f = open(filepath, 'w') 
        for data in dataArray:
            f.writelines(data)
            f.write('\n')
        f.close()

    ########## 学習データ書き出し処理(1次元連想配列用) ##########
    def exportLearningAssArrayCSV(self,fileName = "",dataAssArray = {}) :
        filepath = '.\\LearningData\\' + fileName
        f = open(filepath, 'w') 
        for k, v in dataAssArray.items():
            f.writelines(k + "," + str(v))
            f.write('\n')
        f.close()

    ########## 学習データ書き出し処理(2次元連想配列用) ##########
    def exportLearningAssArrayListCSV(self,fileName = "",dataAssArrayList = {}) :
        filepath = '.\\LearningData\\' + fileName
        f = open(filepath, 'w') 
        for k, v in dataAssArrayList.items():
            for k2, v2 in v.items():
                f.writelines(k + "," + k2 + "," + str(v2))
                f.write('\n')
        f.close()

    ########## 学習データ読み込み処理(2次元配列用) ##########
    def importLearningArrayListCSV(self,fileName = "") :
        filepath = '.\\LearningData\\' + fileName
        f = open(filepath, 'r')
        dataReader = csv.reader(f)
        dataArrayList = []
        for row in dataReader:
            dataArraydataArrayList.append(row)
        f.close()
        # print(dataArray)
        return dataArrayList

    ########## 学習データ読み込み処理(1次元配列用) ##########
    def importLearningArrayCSV(self,fileName = "") :
        filepath = '.\\LearningData\\' + fileName
        f = open(filepath, 'r') 
        dataReader = csv.reader(f)
        dataArray = set()
        for row in dataReader:
            dataArray.add(row[0])
        f.close()
        # print(dataArray)
        return dataArray

    ########## 学習データ読み込み処理(1次元連想配列用) ##########
    def importLearningAssArrayCSV(self,fileName = "") :
        filepath = '.\\LearningData\\' + fileName
        f = open(filepath, 'r') 
        dataReader = csv.reader(f)
        dataAssArray = {}
        for row in dataReader:
            dataAssArray[row[0]]  = int(row[1])
        f.close()
        # print(dataAssArray)
        return dataAssArray

    ########## 学習データ読み込み処理(2次元連想配列用) ##########
    def importLearningAssArrayListCSV(self,fileName = "") :
        filepath = '.\\LearningData\\' + fileName
        f = open(filepath, 'r') 
        dataReader = csv.reader(f)
        dataAssArrayList = {}
        for row in dataReader:
            # dataAssArray = {}
            # dataAssArray[row[1]] = int(row[2])
            if not(row[0] in dataAssArrayList.keys()):
                dataAssArrayList[row[0]]  = defaultdict(int)
            dataAssArrayList[row[0]][row[1]] = int(row[2])
        f.close()
        # print(dataAssArrayList)
        return dataAssArrayList
