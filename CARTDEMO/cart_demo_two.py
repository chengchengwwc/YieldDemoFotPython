#!/usr/bin/env python
# -*- coding:utf-8 -*-


from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.tree import DecisionTreeRegressor



def main():
    #准备数据
    boston = load_boston()
    #获取特征集
    features = boston.data
    #获取房价
    prices = boston.target
    #随机抽取33%的数据作为测试集，其他为训练结合
    train_features, test_features, train_labels, test_labels = train_test_split(features, prices, test_size=0.33,random_state=0)
    #创建CART回归树
    dtr = DecisionTreeRegressor()
    #拟合构造CART回归树
    dtr.fit(train_features,train_labels)
    #预测测试集合中的房价
    predict_price = dtr.predict(test_features)
    #结果评价
    # 回归树二乘偏差均值
    print(mean_squared_error(test_labels,predict_price))
    #回归树绝对值偏差均值
    print(mean_absolute_error(test_labels,predict_price))






if __name__ == "__main__":
    main()