#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris



def main():
    #获取数据集
    iris = load_iris()
    #获取特征集
    features = iris.data
    #获取数据
    labels = iris.target
    #随机抽取33%的数据作为预测集其他作为训练集
    train_features,test_features,train_labels,test_labels = train_test_split(features,labels,test_size=0.33,random_state=0)
    #创建CART分类树
    clf = DecisionTreeClassifier(criterion="gini")
    #拟合构造CART分类树
    clf = clf.fit(train_features,train_labels)
    #用CART分类树实现预测
    test_predict = clf.predict(test_features)
    #预测结果和测试结果做对比
    score = accuracy_score(test_labels,test_predict)
    print (score)






if __name__ == "__main__":
    main()

