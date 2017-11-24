# -*- coding: utf-8 -*-
import FileController
from FileController import FileController

# メイン処理
print('メイン処理開始')
fc = FileController()
fc.importTrainingFile(r'.\TrainingData\*_*.txt')

