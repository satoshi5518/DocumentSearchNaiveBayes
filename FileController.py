# -*- coding: utf-8 -*-
import glob
import re
from janome.tokenizer import Tokenizer

# ファイル操作クラス
class FileController:

    ########## 初期処理 ##########
    def __init__(self) :
        print("初期処理")
        self.trainingDataList = []

    ########## 訓練データ読み込み処理 ##########
    # ファイルを["タグ","名詞","名詞"・・・]フォーマットの多次元配列に変換する。
    def importTrainingFile(self,path = "") :

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
    def importTestFile(self,path = "") :
        testData = []
        t = Tokenizer()
        for line in open(path,'r',encoding="utf-8"):
            for token in t.tokenize(line):
                if token.part_of_speech.split(',')[0] == "名詞" and token.part_of_speech.split(',')[1] == "一般":
                    testData.append(token.surface)
            
        return testData