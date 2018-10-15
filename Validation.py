# coding=utf-8
import pandas as pd
from sklearn.metrics import f1_score


class Validation(object):
    """
    验证器：自动加载validation.csv作为验证数据集
    data: 验证数据
    columns: 20个评价粒度对应的列
    """

    def __init__(self):
        self.data = pd.read_csv("./data/validation.csv", encoding="utf-8")
        self.columns = ['location_traffic_convenience', 'location_distance_from_business_district',
                        'location_easy_to_find',
                        'service_wait_time', 'service_waiters_attitude', 'service_parking_convenience',
                        'service_serving_speed', 'price_level', 'price_cost_effective',
                        'price_discount', 'environment_decoration',
                        'environment_noise', 'environment_space', 'environment_cleaness',
                        'dish_portion', 'dish_taste', 'dish_look', 'dish_recommendation',
                        'others_overall_experience', 'others_willing_to_consume_again']

    def get_data(self) -> pd.DataFrame:
        """
        :return: 返回各项打分均为 -2 的待预测数据集Dataframe，用于存放模型预测结果
        """
        df = self.data.copy()
        for column_name in self.columns:
            df[column_name] = -2
        return df

    def score(self, predict_df: pd.DataFrame) -> float:
        """
        计算预测结果评分
        :param predict_df: 预测数据集
        :return: 20个细粒度的f1平均得分
        """
        score_list = []
        for column_name in self.columns:
            y_true = self.data[column_name].tolist()
            y_pred = predict_df[column_name].tolist()
            score = f1_score(y_true, y_pred, average='macro')
            score_list.append(score)
        return sum(score_list) / len(score_list)
