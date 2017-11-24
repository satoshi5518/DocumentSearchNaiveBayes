# -*- coding: utf-8 -*-
import glob
import re

# ファイル操作クラス
class FileController:

    # 初期処理
    def __init__(self) :
        print("初期処理")

    def importTrainingFile(self,path = "") :
        files = glob.glob(path)

        for file in files:
            print(file)
            tag = re.match(r'\.*_',file)
            print(tag)
            # for line in open(file,'r',encoding="utf-8"):
                # print(line)
