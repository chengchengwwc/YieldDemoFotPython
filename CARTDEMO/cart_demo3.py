#!/usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score



def get_file_detail(file_path):
    test_data = pd.read_csv(file_path)
    print (test_data.info())
    print (test_data.describe())
    print (test_data.describe(include=['O']))
    print (test_data.head())
    print (test_data.tail)



def wash_data(file_path):
    target_data = pd.read_csv(file_path)
    target_data["Age"].fillna(target_data["Age"].mean(),inplace=True)
    target_data["Fare"].fillna(target_data["Fare"].mean(),inplace=True)
    target_data["Embarked"].fillna("S",inplace=True)
    return target_data


def switch_data(target_data):
    """
    使用fit_transform这个函数，它可以将特征向量转化为特征矩阵
    :param target_data:
    :return:
    """
    dvec = DictVectorizer(sparse=False)
    target_data = dvec.fit_transform(target_data.to_dict(orient='record'))
    return target_data


def evaluate_the_results(clf,train_features,train_labels,cv_number):
    """
    K折交叉验证的方法：
    原理是拿出大部分样本进行训练，少量用于分类器的验证，做K次，然后取得平均值
    1 将数据集平均分割成K等分
    2 使用1分数据作为测试数据，其余作为训练数据
    3 计算测试准确率
    4 使用不同的测试集，重复2,3步骤
    :return:
    """
    return np.mean(cross_val_score(clf,train_features,train_labels,cv=cv_number))



def main(test_file_path,train_file_path):
    features = ['Pclass', 'Sex', 'Age','SibSp','Parch','Fare','Embarked']
    train_data = wash_data(train_file_path)
    test_data = wash_data(test_file_path)
    train_features = train_data[features]
    train_labels = train_data["Survived"]
    test_features = test_data[features]
    train_features = switch_data(train_features)
    clf = DecisionTreeClassifier(criterion='entropy')
    clf.fit(train_features,train_labels)
    score = evaluate_the_results(clf,train_features,train_labels,10)
    print (score)




if __name__ == "__main__":
    test_file_path = r"F:\GITHUB\Titanic_Data\test.csv"
    train_file_path = r"F:\GITHUB\Titanic_Data\train.csv"
    main(test_file_path,train_file_path)






