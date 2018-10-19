# coding=utf-8
# version - 1.0
import gensim
import jieba
import jieba.analyse
import pandas as pd
from keras.preprocessing.sequence import pad_sequences


class Preprocessing(object):

    def __init__(self):
        self.data = pd.read_csv("./data/train.csv")
        self.stopwords = [line.strip() for line in open('./dict/stopwords.txt', 'r', encoding='utf-8').readlines()]
        # 预处理参数修改
        self.model_exist = False  # 是否使用已训练的结果
        self.min_count = 1  # 词向量最小频数
        self.size = 100  # 词向量维度
        self.max_length = 50  # 序列最大长度

    def transfer(self):
        """
        预处理方法1.0版本
        实现步骤：分词 - 去停用词 - gensim实现词向量转化 - 统一长度(后端补齐)
        :return: 所有评论的词向量转化结果
        """
        sentences = []
        for comment in self.data["content"]:
            seg_list = jieba.lcut(comment, cut_all=False)
            seg_result = [word for word in seg_list if word not in self.stopwords]
            sentences.append(seg_result)

        if self.model_exist:
            model = gensim.models.Word2Vec.load('./model/word2vec')
        else:
            model = gensim.models.Word2Vec(sentences, min_count=self.min_count, size=self.size)
            model.save('./model/word2vec')

        word_vec_list = [[model[word] for word in sentence] for sentence in sentences]
        return pad_sequences(word_vec_list, dtype='float32', padding='post', truncating='post', maxlen=self.max_length)

    def get_shape(self):
        """
        :return: 每条评论的矩阵大小
        """
        return self.max_length, self.size
