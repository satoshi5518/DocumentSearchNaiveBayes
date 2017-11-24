#coding:utf-8

from collections import defaultdict
import math

class NaiveBayes:

    def __init__(self):
        self.vocabularies    = set() # 重複なしの語彙
        self.categories      = set() # 重複なしのカテゴリ
        self.category_count  = {}    # カテゴリの出現回数, category_count[cat]
        self.word_count      = {}    # カテゴリ毎の単語出現回数, word_count[cat]


    def train(self, data):
        self.category_count = defaultdict(lambda: 0)

        for d in data:
            category = d[0]
            self.categories.add(category) # カテゴリの追加
            self.category_count[category] += 1

            for word in d[1:]: # 語彙の追加
                self.vocabularies.add(word)

        for category in self.categories:
            self.word_count[category]  = defaultdict(lambda: 0)

        for d in data:
            category = d[0]
            for word in d[1:]:
                self.word_count[category][word] += 1


    def word_probability(self, word, category):
        '''単語が与えられた時のカテゴリである確率, P(word|cat)'''
        # ラプラススムージング を適用
        word_count       = self.word_count[category][word] + 1
        vocabulary_count = sum(self.word_count[category].values()) + len(self.vocabularies)
        return float(word_count) / float(vocabulary_count)


    def score(self, words, category):
        '''文書(単語)が与えられたときのカテゴリである確率'''
        documents_count = sum(self.category_count.values())
        score = math.log(float(self.category_count[category]) / documents_count)

        for word in words:
            score += math.log(self.word_probability(word, category))

        # logの底が10なのでマイナスになるから+にしちゃう
        return score * (-1)


    def classify(self, words):
        '''P(cat|doc)が最も大きなカテゴリを返す'''
        best  = None
        value = 0

        for category in self.categories:
            v = self.score(words, category)
            if v > value:
                best  = category
                value = v
        return best