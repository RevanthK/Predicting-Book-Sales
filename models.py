# Revanth Korrapolu
# December 15, 2019
# Implementation of 4 different models:
# 1. Linear Regression
# 2. K Nearest Neighbors
# 3. Neural Network
# 4. Learning to Place (new model)

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

def LinearRegression(bookinfo, pageview):

    X = pageview
    y = bookinfo

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    classifier = LinearRegression().fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

def KNN(bookinfo, pageview):

    X = pageview
    y = bookinfo

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

def NeuralNetwork(bookinfo, pageview):

    X = pageview
    y = bookinfo

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
    mlp.fit(X_train, y_train.values.ravel())

    predictions = mlp.predict(X_test)

    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))

def LearningToPlace(bookinfo, pageview):

    print("TODO")

def main():
    book_info = pd.read_csv("DATA/isbnToInfo.csv")
    pageview = pd.read_csv("DATA/pageview.csv")

    LinearRegression(book_info, pageview)
    KNN(book_info, pageview)
    NeuralNetwork(book_info, pageview)
    LearningToPlace(book_info, pageview)

if __name__ == "__main__":
    main()



