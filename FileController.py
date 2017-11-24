# -*- coding: utf-8 -*-
import glob
import re

# ファイル操作クラス
class FileController:

    # 初期処理
    def __init__(self) :
        print("初期処理")
        self.trainingDataList = [[]]

    def importTrainingFile(self,path = "") :
        files = glob.glob(path)

        for file in files:

            trainingData = []
            # print(file)
            tag = re.search(r'_.*?_',file).group().replace('_','')
            # print(tag)
            trainingData.append(tag)
            
            for line in open(file,'r',encoding="utf-8"):
                # print(line)
                # self.trainingData.append(line)
                trainingData.append(line)
            
            self.trainingDataList.append(trainingData)
