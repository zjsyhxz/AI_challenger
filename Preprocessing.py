# coding=utf-8
# version - 1.1
import gensim
import jieba
import jieba.analyse
import pandas as pd
from keras.preprocessing.sequence import pad_sequences


class Preprocessing(object):

    def __init__(self, file_path, head_num=None):
        """
        :param file_path: 数据集文件路径
        :param head_num: 截取开头部分数据（默认为None表示不截取）
        """
        self.data = pd.read_csv(file_path)
        if head_num is not None:
            self.data = self.data.head(head_num)
        self.stopwords = [line.strip() for line in open('./dict/stopwords.txt', 'r', encoding='utf-8').readlines()]
        self.columns = self.data.columns[-20:].tolist()  # 20个细粒度列名
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

    def get_labels(self, column_name):
        """
        :param column_name: 列名
        :return: 作为输入数据的标签
        """
        return self.data[column_name].tolist()
